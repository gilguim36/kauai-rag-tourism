import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

DB_DIR = "db"

def main():
    api_key = input("Digite sua OpenAI API Key (sk-...): ").strip()
    os.environ["OPENAI_API_KEY"] = api_key

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    docs = vectordb.similarity_search("Poipu Beach", k=3)
    for d in docs:
        print(d.page_content[:200], d.metadata)

if __name__ == "__main__":
    main()