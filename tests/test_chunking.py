from app.chunking import chunk_text

def test_chunk_text_returns_multiple_chunks():
    text = "alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi"
    chunks = chunk_text(text, chunk_size=6, overlap=2)

    assert len(chunks) >= 2
    assert all(isinstance(chunk, str) for chunk in chunks)
    assert "alpha" in chunks[0].lower()