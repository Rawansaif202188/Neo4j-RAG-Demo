from neo4j import GraphDatabase


class Neo4jClient:
    """Handle Neo4j database operations for the RAG system."""

    def __init__(
        self,
        uri: str,
        username: str,
        password: str
    ):
        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def close(self):
        """Close the Neo4j connection."""

        self.driver.close()

    def create_vector_index(self, dimensions: int):
        """Create a vector index for document embeddings."""

        query = f"""
        CREATE VECTOR INDEX document_chunk_embeddings IF NOT EXISTS
        FOR (d:DocumentChunk)
        ON d.embedding
        OPTIONS {{
            indexConfig: {{
                `vector.dimensions`: {dimensions},
                `vector.similarity_function`: 'cosine'
            }}
        }}
        """

        with self.driver.session() as session:
            session.run(query)

    def store_document_chunk(
        self,
        chunk_id: str,
        chunk_text: str,
        embedding: list[float]
    ):
        """Store a document chunk and its embedding."""

        query = """
        MERGE (d:DocumentChunk {id: $id})
        SET d.text = $text,
            d.embedding = $embedding
        """

        with self.driver.session() as session:
            session.run(
                query,
                id=chunk_id,
                text=chunk_text,
                embedding=embedding
            )

    def retrieve_similar_chunks(
        self,
        query_embedding: list[float],
        limit: int = 5
    ):
        """Retrieve similar chunks using Neo4j vector search."""

        query = """
        MATCH (node:DocumentChunk)
        SEARCH node IN (
            VECTOR INDEX document_chunk_embeddings
            FOR $query_embedding
            LIMIT $limit
        ) SCORE AS score

        RETURN node.id AS id,
               node.text AS text,
               score
        ORDER BY score DESC
        """

        with self.driver.session() as session:
            result = session.run(
                query,
                limit=limit,
                query_embedding=query_embedding
            )

            return [record.data() for record in result]