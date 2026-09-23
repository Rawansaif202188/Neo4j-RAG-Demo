from app.rag_pipeline import RAGPipeline


def test_chunk_documents():
    pipeline = RAGPipeline.__new__(RAGPipeline)

    documents = [
        "First paragraph.\nSecond paragraph.",
        "Third paragraph."
    ]

    chunks = pipeline.chunk_documents(documents)

    assert chunks == [
        "First paragraph.",
        "Second paragraph.",
        "Third paragraph."
    ]