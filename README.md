# Neo4j RAG Demo

A beginner-friendly Retrieval-Augmented Generation (RAG) pipeline built with **Python, Neo4j, OpenAI embeddings, and an OpenAI LLM**.

The project demonstrates how a RAG system retrieves semantically relevant information from a vector database and uses the retrieved context to generate an answer.

> **Educational project — not production-ready.**

## Architecture

```text
Documents
    ↓
Document Chunking
    ↓
OpenAI Embeddings
    ↓
Neo4j Vector Database
    ↓
Semantic Retrieval
    ↓
Similarity Threshold
    ↓
Retrieved Context
    ↓
OpenAI LLM
    ↓
Final Answer
```

## Features

* Real OpenAI embeddings
* Neo4j as a vector database
* Semantic vector search using cosine similarity
* Similarity threshold to filter weak retrieval results
* LLM-based answer generation
* Retrieval context displayed with similarity scores
* Environment variables for configuration
* Unit tests for core components
* Example of good and poor retrieval quality

## Project Structure

```text
my-neo4j-rag-demo/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── neo4j_client.py
│   ├── rag_pipeline.py
│   └── main.py
├── data/
│   └── sample_documents.txt
├── tests/
│   ├── __init__.py
│   ├── test_chunking.py
│   └── test_retrieval.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── run_demo.py
```

## Main Components

* **`app/config.py`** — Loads configuration and environment variables.
* **`app/data_loader.py`** — Loads the sample documents.
* **`app/embeddings.py`** — Generates real embeddings using OpenAI.
* **`app/neo4j_client.py`** — Connects to Neo4j, stores embeddings, and performs vector search.
* **`app/generator.py`** — Generates answers using the retrieved context and an OpenAI LLM.
* **`app/rag_pipeline.py`** — Coordinates document ingestion, retrieval, filtering, and generation.
* **`app/main.py`** — Runs the interactive RAG demo.
* **`data/sample_documents.txt`** — Sample knowledge base used by the demo.
* **`tests/`** — Unit tests for document chunking and retrieval.
* **`.env.example`** — Example environment variable configuration.
* **`requirements.txt`** — Project dependencies.

## Requirements

* Python 3.10+
* Neo4j database
* OpenAI API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rawansaif202188/Neo4j-RAG-Demo.git
cd Neo4j-RAG-Demo
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example`:

```text
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password_here

OPENAI_API_KEY=your_openai_api_key_here
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_LLM_MODEL=gpt-4o-mini
```

> Never commit your `.env` file or expose your API keys.

## Running the Demo

Run:

```bash
python run_demo.py
```

The application will:

1. Load the sample documents.
2. Split them into document chunks.
3. Generate embeddings.
4. Store the chunks and embeddings in Neo4j.
5. Generate an embedding for the user's question.
6. Retrieve semantically similar chunks.
7. Filter results using a similarity threshold.
8. Send the retrieved context to the LLM.
9. Generate the final answer.

## Retrieval Threshold

The demo uses a similarity threshold of **0.65** to filter out weak retrieval results.

This value is an experimental setting for this demo and is **not a universal threshold** for all RAG systems.

If no retrieved chunks meet the threshold, the system returns:

```text
There is not enough information in the knowledge base.
```

This prevents the LLM from receiving irrelevant context.

## Example

### Good Retrieval

Question:

```text
How do computers understand human language?
```

The system retrieves relevant information about:

* Natural Language Processing
* Semantic search
* Artificial Intelligence
* Generative AI

The retrieved chunks are passed to the LLM as context.

### Poor Retrieval

Question:

```text
What are the best restaurants in Riyadh?
```

The question is unrelated to the knowledge base.

The retrieved similarity scores remain below the threshold, so the system returns:

```text
There is not enough information in the knowledge base.
```

This demonstrates how retrieval filtering can prevent irrelevant information from being passed to the LLM.

## Testing

Run the test suite with:

```bash
pytest
```

Expected result:

```text
2 passed
```

The tests cover:

* Document chunking
* Retrieval behavior

The tests use mocked components where appropriate so they do not require a live Neo4j database or OpenAI API call.

## Limitations

This project is intentionally simple and designed for learning and demonstration.

Current limitations include:

* Simple paragraph-based chunking
* Small sample dataset
* Fixed similarity threshold
* No conversation memory
* No metadata filtering
* No advanced reranking
* No production monitoring or evaluation framework

## Future Improvements

Possible improvements include:

* More advanced document chunking
* Larger knowledge bases
* Metadata-based filtering
* Reranking retrieved results
* Retrieval evaluation metrics
* Conversation memory
* Support for additional document formats
* Production deployment and monitoring

## License

This project is intended for educational and demonstration purposes.
