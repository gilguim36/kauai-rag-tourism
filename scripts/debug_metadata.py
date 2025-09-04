import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

DB_DIR = "db"

def main():
    api_key = input("Digite sua OpenAI API Key (sk-...): ").strip()
    os.environ["OPENAI_API_KEY"] = api_key

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    # Pegar vários docs do DB
    docs = vectordb.similarity_search("Kauai", k=20)

    categories = set()
    for doc in docs:
        if "category" in doc.metadata:
            categories.add(doc.metadata["category"])

    print("Categorias encontradas no DB:", categories)

if __name__ == "__main__":
    main()