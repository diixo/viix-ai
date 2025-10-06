import uvicorn
import sys
import os
import json
import requests
from fastapi import FastAPI
from server.searching_server import SearchingServer
from server.schemas import StrRequestModel, ContentItemModel, DialogueModel, DialogueParams
from typing import List, Optional
import logging


app = FastAPI()

searching_server_global = SearchingServer()


######################################################
def searching_server():
    global searching_server_global
    return searching_server_global


@app.post("/ai-search", response_model=List[ContentItemModel])
async def ai_search(input_request: StrRequestModel):
    return searching_server().search(input_request.str_request)


@app.post("/page-to-index")
async def page_to_index(input_request: StrRequestModel):
    searching_server().page_to_index(input_request.str_request)
    return { "status": "200" }


@app.post("/text-to-index")
async def text_to_index(input_request: StrRequestModel):
    searching_server().text_to_index(input_request.str_request)
    return { "status": "200" }


@app.post("/new-message")
async def new_message(dialogue: DialogueParams):
    if dialogue.dialogue_type in {"developer", "manager", "auditor",}:
        print("new message:", dialogue.message_str)
    return { "status": "200" }


@app.post("/get-answer", response_model=Optional[StrRequestModel])
async def get_answer(dialogue: DialogueParams):
    return StrRequestModel(
        str_request="You should ask your Line Manager to assign task on you, or create new one by yourself."
    )


@app.post("/get-dialogue", response_model=Optional[DialogueModel])
async def get_dialogue(dialogue: DialogueParams):
    if dialogue.dialogue_type in {"developer", "manager", "auditor",}:
        dialogue = DialogueModel(
            assistant = ["Hi, I am development Assistant.", "Do you have any assigned tickets on you?"],
            user =      ["Hello", "I have finished all development activities."]
        )
        return dialogue
    else:
        return None


@app.post("/new-dialogue")
async def new_dialogue(dialogue: DialogueParams):
    if dialogue.dialogue_type in {"developer", "manager", "auditor",}:
        print("::new_dialogue:", dialogue.dialogue_type)
    return { "status": "200" }


if __name__ == "__main__":
    try:
        uvicorn.run(
            "server_api:app",
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8001)),
            log_level="info")
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        print(f"Exception with force stop: {e}", file=sys.stderr)
        #parsing_server_global.stop()
