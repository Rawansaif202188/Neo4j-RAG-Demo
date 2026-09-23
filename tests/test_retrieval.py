from app.rag_pipeline import RAGPipeline


def test_retrieval_returns_results(monkeypatch):
    pipeline = RAGPipeline.__new__(RAGPipeline)

    class FakeNeo4jClient:
        def retrieve_similar_chunks(
            self,
            query_embedding,
            limit=5
        ):
            return [
                {
                    "id": "1",
                    "text": "NLP enables computers to understand language.",
                    "score": 0.80
                },
                {
                    "id": "2",
                    "text": "AI systems can process human language.",
                    "score": 0.70
                }
            ]

    pipeline.neo4j_client = FakeNeo4jClient()

    monkeypatch.setattr(
        "app.rag_pipeline.generate_embedding",
        lambda text: [0.1, 0.2, 0.3]
    )

    results = pipeline.query("What is NLP?")

    assert len(results) == 2
    assert results[0]["score"] > results[1]["score"]