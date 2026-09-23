import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    NEO4J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    OPENAI_EMBEDDING_MODEL = os.getenv(
        "OPENAI_EMBEDDING_MODEL",
        "text-embedding-3-small"
    )

    OPENAI_LLM_MODEL = os.getenv(
        "OPENAI_LLM_MODEL",
        "gpt-4o-mini"
    )

    DOCUMENTS_PATH = os.getenv(
        "DOCUMENTS_PATH",
        "data/sample_documents.txt"
    )