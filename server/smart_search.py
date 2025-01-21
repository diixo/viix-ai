
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
        return self.model.encode(texts)
    
    def add_texts_to_index(self, texts):
        vector = self.texts_to_vector(texts)
        self.index.add(vector)

    def create_index(self, texts: list):
        # Создание индекса FAISS
        #dimension = embeddings.shape[1]  # Размерность эмбеддингов
        dimension = 384
        self.index = faiss.IndexFlatL2(dimension)  # Использование L2 (евклидова) метрики

        # Добавление эмбеддингов в индекс
        self.add_texts_to_index(texts)

    def write_index(self, filepath: str):
        faiss.write_index(self.index, filepath)

    def add_str_to_index(self, text: str):
        self.add_texts_to_index([ text ])

    def search(self, query_text: str):
        # Преобразование запроса в эмбеддинг
        query_embedding = self.model.encode([query_text])

        # Поиск ближайших соседей
        k = 20  # Количество ближайших соседей для поиска
        distances, indices = self.index.search(query_embedding, k)

        if indices.size > 0:
            return indices[0].tolist(), distances[0].tolist()
        return [], []
