from app.config import Config
from app.rag_pipeline import RAGPipeline


def main():
    """Run the interactive RAG demo."""

    rag_pipeline = RAGPipeline(
        neo4j_uri=Config.NEO4J_URI,
        neo4j_username=Config.NEO4J_USERNAME,
        neo4j_password=Config.NEO4J_PASSWORD
    )

    try:
        print("Loading documents...")
        rag_pipeline.ingest_documents(Config.DOCUMENTS_PATH)

        print("Documents successfully stored in Neo4j.")
        print("\nRAG Demo is ready!")

        while True:
            user_query = input(
                "\nEnter your question (or type 'exit' to quit): "
            )

            if user_query.lower() == "exit":
                break

            result = rag_pipeline.answer_question(user_query)

            print("\nAnswer:")
            print(result["answer"])

            print("\nRetrieved Context:")

            if not result["sources"]:
                print("No relevant documents found.")
                continue

            for source in result["sources"]:
                print(
                    f"\nScore: {source['score']:.4f}"
                    f"\n{source['text']}"
                )

    finally:
        rag_pipeline.close()


if __name__ == "__main__":
    main()