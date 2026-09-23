from app.rag_pipeline import RAGPipeline

def main():
    # Initialize the RAG pipeline
    rag_pipeline = RAGPipeline()

    # Load documents and prepare for querying
    rag_pipeline.load_documents()

    while True:
        # Get user input for querying
        user_query = input("Enter your query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        
        # Perform retrieval and generate response
        response = rag_pipeline.query(user_query)
        print("Response:", response)

if __name__ == "__main__":
    main()