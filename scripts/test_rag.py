import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

def main():
    # API Key do usuário
    api_key = input("Digite sua OpenAI API Key (sk-...): ").strip()
    os.environ["OPENAI_API_KEY"] = api_key

    # Carregar banco vetorial
    print("Carregando banco vetorial...")
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # Modelo LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Pipeline RAG
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Loop interativo
    print("\nDigite sua pergunta sobre Kaua’i (ou 'exit' para sair):")
    while True:
        query = input("> ")
        if query.lower() in ["exit", "quit", "sair"]:
            break
        answer = qa.run(query)
        print("\nResposta:", answer, "\n")

if __name__ == "__main__":
    main()