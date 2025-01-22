
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
from pathlib import Path


class SmartSearch:

    def __init__(self) -> None:
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None

    def open_file(self, filepath: str):
        path = Path(filepath)
        if path.exists():
            self.index = faiss.read_index(filepath)
            return True
        return False
    
    def texts_to_vector(self, texts):
        if self.model: 
            return self.model.encode(texts)
        return None
    
    def add_texts_to_index(self, texts):
        if self.index:
            vector = self.texts_to_vector(texts)
            if vector is not None:
                self.index.add(vector)

    def create_index(self, texts: list):
        # create index FAISS
        #dimension = embeddings.shape[1]
        dimension = 384
        if self.model:
            dimension = self.model.output_size()
            self.index = faiss.IndexFlatL2(dimension)  # Using L2 (Euclidean) metrics

        self.add_texts_to_index(texts)

    def write_index(self, filepath: str):
        if self.index:
            faiss.write_index(self.index, filepath)

    def add_str_to_index(self, text: str):
        self.add_texts_to_index([ text ])

    def search(self, query_text: str):
        if self.model:
            query_embedding = self.model.encode([query_text])

            k = 50
            distances, indices = self.index.search(query_embedding, k)

            if indices.size > 0:
                return indices[0].tolist(), distances[0].tolist()
        return [], []
