
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from collections import deque
from typing import List
from server.schemas import Message
from dataclasses import dataclass, field


@dataclass
class Conversation:
    system_prompt: str
    conversation_history: deque = field(default_factory=lambda: deque(maxlen=512))


class Dialogue_gpt2:

    def __init__(self):
        model_dir = "server/models/gpt2-babi"
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
        self.model = GPT2LMHeadModel.from_pretrained(model_dir)


    def build_prompt(self, conv: Conversation, user_message):
        # Create prompt for model in format:
        """
        System:
        {system_message}
        User:
        {user_message}
        Assistant:
        {response}
        """
        prompt = ""

        for role, content in conv.conversation_history:
            if role == "user":
                prompt += f"User:\n{content}\n"
            elif role == "assistant":
                prompt += f"Assistant:\n{content}\n"

        if user_message:
            prompt += f"User:\n{user_message}\n"
        prompt += f"Assistant:\n"
        return prompt


    def generate_response(self, prompt, max_new_tokens=100):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=self.tokenizer.eos_token_id
        )[0]
        text = self.tokenizer.decode(outputs, skip_special_tokens=True)
        marker = "Assistant:"
        if marker in text:
            text = text.split(marker)[-1].strip()
        return text


    def handle_user_message(self, conv: Conversation, user_message=None):

        system = f"System:\n{conv.system_prompt}\n"

        # Build prompt
        prompt = self.build_prompt(conv, user_message)

        # create response
        assistant_reply = self.generate_response(system + prompt)

        # Update history by pair: user+prompt.
        if user_message:
            conv.conversation_history.append(("User", user_message))
        else: # init, appand prompt as welcole-message
            assistant_reply = prompt + assistant_reply

        conv.conversation_history.append(("Assistant", assistant_reply))
        return assistant_reply


    def get_messages(self, conv: Conversation):
        return [
            Message(role=role, utterance=msg.replace("\n", " ").removeprefix(f"{role}: ").strip())
            for role, msg in conv.conversation_history
        ]


    def get_last_answer(self, conv: Conversation):
        role, msg = conv.conversation_history[-1]
        return Message(role=role, utterance=msg.replace("\n", " ").removeprefix(f"{role}: ").strip())


    def clear(self, conv: Conversation):
        conv.conversation_history.clear()
        self.handle_user_message(conv)

