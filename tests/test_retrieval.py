from app.retrieval import build_context

def test_build_context_creates_readable_string():
    matches = [
        {"document_index": "0", "similarity": 0.91, "text": "This is a matching chunk."},
        {"document_index": "1", "similarity": 0.70, "text": "This is another chunk."},
    ]

    context = build_context(matches)

    assert "Chunk 1" in context
    assert "This is a matching chunk." in context