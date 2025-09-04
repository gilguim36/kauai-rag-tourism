import os
import gradio as gr
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

DEBUG = True  # mude para False se não quiser logs no terminal

# Estado de carregamento
def loading_state():
    return "⏳ Processing your question, please wait..."

# Função principal do app
def answer_question(api_key, question, category):
    if not api_key or not api_key.startswith("sk-"):
        return "⚠️ Please provide a valid OpenAI API Key (sk-...)."

    os.environ["OPENAI_API_KEY"] = api_key

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)

    # Se categoria selecionada ≠ All, aplicar filtro
    if category and category != "All":
        retriever = vectordb.as_retriever(
            search_kwargs={"k": 3, "filter": {"category": category}}
        )
    else:
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, streaming=True)

    # Debug opcional
    if DEBUG:
        results = retriever.get_relevant_documents(question)
        print("\n=== DEBUG: docs recuperados ===")
        for r in results:
            print(f"Texto: {r.page_content[:80]}... | Metadata: {r.metadata}")
        print("=== Fim DEBUG ===\n")

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    try:
        answer = qa.run(question)

        if (
            not answer
            or answer.strip() == ""
            or "I don't have information" in answer
            or "I’m sorry" in answer
            or "No information" in answer
        ):
            return f"⚠️ No results found for category *{category}*. Try another one."

        return answer
    except Exception:
        return f"⚠️ No results found for category *{category}*. Try another one."

# Interface Gradio
with gr.Blocks(theme="soft") as demo:
    gr.Markdown(
        """
        # 🌺 Kaua’i RAG Tourism — Travel Assistant  
        Ask me anything about Kaua’i (Hawaii)!  
        I combine structured knowledge (JSON) + tourist guides (PDF) to help you plan your trip.  
        ---
        """
    )

    with gr.Row():
        api_key = gr.Textbox(
            label="🔑 OpenAI API Key",
            type="password",
            placeholder="Enter your OpenAI API Key (sk-...)",
        )

    with gr.Row():
        question = gr.Textbox(
            label="❓ Your Question",
            placeholder="Example: What is Waimea Canyon?",
        )

    with gr.Row():
        category = gr.Dropdown(
            choices=[
                "All",
                "Nature",
                "Nature / Adventure",
                "Beach",
                "Waterfall",
                "Hiking / Park",
                "Botanical Garden",
                "Natural Attraction",
                "Historic / Nature",
                "Natural Pool",
            ],
            value="All",
            label="🏷️ Filter by Category",
        )

    with gr.Row():
        submit_btn = gr.Button("✨ Ask")

    answer = gr.Markdown(label="Answer")

    examples = gr.Examples(
        examples=[
            ["What is Waimea Canyon?"],
            ["What is the best time to visit Kaua’i?"],
            ["Which beaches are the most famous in Kaua’i?"],
            ["Tell me about hiking trails in Kaua’i."],
        ],
        inputs=[question],
    )

    # Ao clicar: mostra estado de carregamento -> executa a query
    submit_btn.click(
        fn=loading_state,
        inputs=[],
        outputs=answer
    ).then(
        fn=answer_question,
        inputs=[api_key, question, category],
        outputs=answer,
        show_progress=True
    )

if __name__ == "__main__":
    demo.launch()