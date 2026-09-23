from neo4j import GraphDatabase
import os

class Neo4jClient:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def store_document_chunk(self, chunk_id, chunk_text, embedding):
        with self.driver.session() as session:
            session.run(
                "CREATE (d:DocumentChunk {id: $id, text: $text, embedding: $embedding})",
                id=chunk_id,
                text=chunk_text,
                embedding=embedding
            )

    def retrieve_similar_chunks(self, query_embedding, limit=5):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (d:DocumentChunk) "
                "WITH d, gds.alpha.similarity.cosine(d.embedding, $query_embedding) AS similarity "
                "WHERE similarity IS NOT NULL "
                "RETURN d ORDER BY similarity DESC LIMIT $limit",
                query_embedding=query_embedding,
                limit=limit
            )
            return [record["d"] for record in result]