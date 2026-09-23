# My Neo4j RAG Demo

This project demonstrates a lightweight Retrieval-Augmented Generation (RAG) pipeline using Python and Neo4j as the vector database. The RAG architecture combines traditional retrieval methods with generative models to enhance the quality of responses based on retrieved information.

## Project Structure

```
my-neo4j-rag-demo
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── embeddings.py
│   ├── neo4j_client.py
│   ├── rag_pipeline.py
│   └── main.py
├── data
│   └── sample_documents.txt
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── run_demo.py
```

### Description of Files

- **app/__init__.py**: Initializes the app package.
- **app/config.py**: Contains configuration settings and loads environment variables.
- **app/data_loader.py**: Implements functions to read and prepare documents for chunking.
- **app/embeddings.py**: Generates embeddings for document chunks using a specified model/API.
- **app/neo4j_client.py**: Manages the connection to the Neo4j database for storing and retrieving data.
- **app/rag_pipeline.py**: Orchestrates the RAG pipeline, coordinating all components.
- **app/main.py**: Entry point for running the demo and handling user queries.
- **data/sample_documents.txt**: Contains sample documents for the demo.
- **.env.example**: Template for environment variables.
- **.gitignore**: Specifies files to ignore in version control.
- **requirements.txt**: Lists project dependencies.
- **run_demo.py**: Script to execute the demo and display results.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-neo4j-rag-demo
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables by copying `.env.example` to `.env` and filling in the necessary values.

## Running the Demo

To run the demo, execute the following command:
```
python run_demo.py
```

Follow the prompts to interact with the RAG pipeline and see how it retrieves and generates responses based on the provided documents.

## Conclusion

This project serves as a foundational example of how to implement a RAG pipeline using Neo4j and Python. It can be extended and modified to suit more complex use cases and larger datasets.