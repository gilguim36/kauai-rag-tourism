import os
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

# Caminhos dos arquivos
JSON_PATH = os.path.join("data", "kauai.json")
PDF_PATH = os.path.join("data", "kauai-maps.pdf")
DB_DIR = "db"

def load_json(path):
    """Carrega JSON manualmente e transforma em documentos com metadata"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = []
    for item in data:
        text = (
            f"Name: {item['name']}\n"
            f"Category: {item['category']}\n"
            f"Description: {item['description']}\n"
            f"Recommended Duration: {item['recommended_duration']}\n"
            f"Tips: {item['tips']}\n"
            f"Keywords: {item['category']}"
        )
        docs.append(
            Document(
                page_content=text,
                metadata={"source": "json", "category": item["category"]}
            )
        )
    return docs

def load_pdf(path):
    """Carrega PDF e transforma em documentos com metadata"""
    loader = PyPDFLoader(path)
    docs = loader.load()
    for doc in docs:
        doc.metadata["source"] = "pdf"
    return docs

def main():
    # API Key deve ser informada pelo usuário
    api_key = input("Digite sua OpenAI API Key (sk-...): ").strip()
    os.environ["OPENAI_API_KEY"] = api_key

    print("Carregando JSON...")
    json_docs = load_json(JSON_PATH)

    print("Carregando PDF...")
    pdf_docs = load_pdf(PDF_PATH)

    all_docs = json_docs + pdf_docs
    print(f"Total de documentos carregados: {len(all_docs)}")

    # Quebra de texto em chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(all_docs)
    print(f"Total de chunks após split: {len(split_docs)}")

    # Criar embeddings e banco vetorial
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    print(f"Indexação concluída! Banco salvo em: {DB_DIR}")

if __name__ == "__main__":
    main()