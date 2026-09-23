from openai import OpenAI

from app.config import Config


client = OpenAI(api_key=Config.OPENAI_API_KEY)


def generate_embedding(text: str) -> list[float]:
    """Generate an embedding for a single text."""

    response = client.embeddings.create(
        model=Config.OPENAI_EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding


def generate_embeddings(
    document_chunks: list[str]
) -> list[list[float]]:
    """Generate embeddings for multiple document chunks."""

    if not document_chunks:
        return []

    response = client.embeddings.create(
        model=Config.OPENAI_EMBEDDING_MODEL,
        input=document_chunks
    )

    return [
        item.embedding
        for item in response.data
    ]