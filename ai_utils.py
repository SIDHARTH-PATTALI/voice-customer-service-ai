import time
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from voice_utils import speak
from config import GROQ_API_KEY

def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile"
    )

def ask_ai_question(llm, retriever, question, return_only=False):
    prompt = ChatPromptTemplate.from_template("""
    You are a customer service agent. So make your sentence polite and helpful.
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.

    <context>
    {context}
    </context>

    Question: {input}
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": question})

    answer = response.get(
        "answer",
        "Sorry, I couldn’t find the right answer to your question. "
        "If you'd like to speak to a human customer service agent, please press 9 or say 'agent'."
    )
    if return_only:
        return answer

    print("🧠", answer)
    speak(answer)
