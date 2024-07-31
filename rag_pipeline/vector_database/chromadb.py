import chromadb
import uuid
from typing import List
from openai import OpenAI
from rag_pipeline.config import settings


class ChromaDBVectorDatabase:
    def __init__(self,
                 collection_name,
                 chromadb_directory: str,
                 embedding_model: str = "text-embedding-3-large"):
        # embedding models
        self.embedding_model = embedding_model
        self._embedding_client = self._create_embedding_client()

        # client and collection for chromadb
        self.chromadb_directory = chromadb_directory
        self._client = self._create_client()
        self.collection = self._client.get_or_create_collection(name=collection_name)

    def _create_client(self):
        client = chromadb.PersistentClient(
            path=self.chromadb_directory
        )
        return client

    @staticmethod
    def _create_embedding_client():
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        return client

    def create(self, documents: List[str], metadatas=None):
        """
        Create new entries in the vector database.
        """
        embeddings = self.embed_texts(text_inputs=documents)
        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            ids=[uuid.uuid4().hex for _ in range(len(documents))],
            metadatas=metadatas
        )

    def query(self, query_text, n_results: int = 5):
        """
        Query the vector database.
        """
        query_embeddings = self.embed_texts(query_text)
        return self.collection.query(
            query_embeddings=query_embeddings,
            n_results=n_results
        )

    def embed_texts(self, text_inputs: List[str]):
        embedding_output = self._embedding_client.embeddings.create(
            model=self.embedding_model, input=text_inputs)
        embeddings = [embedding_data.embedding for embedding_data in embedding_output.data]
        return embeddings
