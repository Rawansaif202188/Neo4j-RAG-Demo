from data_loader import load_documents
from embeddings import generate_embeddings
from neo4j_client import Neo4jClient
from typing import List

class RAGPipeline:
    def __init__(self, neo4j_uri: str, neo4j_user: str, neo4j_password: str):
        self.neo4j_client = Neo4jClient(neo4j_uri, neo4j_user, neo4j_password)

    def run(self, document_file: str, query: str) -> str:
        documents = load_documents(document_file)
        chunks = self.chunk_documents(documents)
        embeddings = generate_embeddings(chunks)
        
        self.store_in_neo4j(chunks, embeddings)
        results = self.retrieve_from_neo4j(query)
        
        return results

    def chunk_documents(self, documents: List[str]) -> List[str]:
        # Simple chunking logic (can be improved)
        return [doc for document in documents for doc in document.split('\n') if doc]

    def store_in_neo4j(self, chunks: List[str], embeddings: List[List[float]]):
        for chunk, embedding in zip(chunks, embeddings):
            self.neo4j_client.store_chunk(chunk, embedding)

    def retrieve_from_neo4j(self, query: str) -> str:
        return self.neo4j_client.semantic_retrieve(query)