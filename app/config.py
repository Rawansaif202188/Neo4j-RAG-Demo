import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    NE04J_URI = os.getenv("NEO4J_URI")
    NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "default_model")
    DOCUMENTS_PATH = os.getenv("DOCUMENTS_PATH", "data/sample_documents.txt")