from app.data_loader import load_documents
from app.embeddings import generate_embedding, generate_embeddings
from app.generator import generate_answer
from app.neo4j_client import Neo4jClient


class RAGPipeline:
    """Coordinate document ingestion, retrieval, and generation."""

    def __init__(
        self,
        neo4j_uri: str,
        neo4j_username: str,
        neo4j_password: str
    ):
        self.neo4j_client = Neo4jClient(
            neo4j_uri,
            neo4j_username,
            neo4j_password
        )

    def ingest_documents(self, document_file: str):
        """Load, chunk, embed, and store documents in Neo4j."""

        documents = load_documents(document_file)

        chunks = self.chunk_documents(documents)

        embeddings = generate_embeddings(chunks)

        if not embeddings:
            return

        self.neo4j_client.create_vector_index(
            dimensions=len(embeddings[0])
        )

        self.store_in_neo4j(chunks, embeddings)

    def query(self, user_query: str, limit: int = 5):
        """Retrieve similar document chunks for a user query."""

        query_embedding = generate_embedding(user_query)

        return self.neo4j_client.retrieve_similar_chunks(
            query_embedding,
            limit=limit
        )

    def answer_question(self, user_query: str, limit: int = 5):
        """Retrieve relevant context and generate an answer."""

        results = self.query(user_query, limit=limit)

        similarity_threshold = 0.65

        filtered_results = [
            result
            for result in results
            if result["score"] >= similarity_threshold
        ]

        if not filtered_results:
            return {
                "answer": (
                    "There is not enough information "
                    "in the knowledge base."
                ),
                "sources": []
            }

        answer = generate_answer(
            question=user_query,
            context=filtered_results
        )

        return {
            "answer": answer,
            "sources": filtered_results
        }

    def chunk_documents(
        self,
        documents: list[str]
    ) -> list[str]:
        """Create simple chunks from loaded documents."""

        chunks = []

        for document in documents:
            paragraphs = [
                paragraph.strip()
                for paragraph in document.split("\n")
                if paragraph.strip()
            ]

            chunks.extend(paragraphs)

        return chunks

    def store_in_neo4j(
        self,
        chunks: list[str],
        embeddings: list[list[float]]
    ):
        """Store document chunks and embeddings in Neo4j."""

        for index, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):
            self.neo4j_client.store_document_chunk(
                chunk_id=str(index),
                chunk_text=chunk,
                embedding=embedding
            )

    def close(self):
        """Close the Neo4j connection."""

        self.neo4j_client.close()