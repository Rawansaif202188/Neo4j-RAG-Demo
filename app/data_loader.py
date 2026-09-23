def load_documents(file_path):
    documents = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            documents.append(line.strip())
    return documents

def prepare_documents(documents):
    # Here you can implement any preprocessing steps if needed
    return documents

def load_and_prepare_documents(data_directory):
    documents = load_documents(data_directory)
    return prepare_documents(documents)