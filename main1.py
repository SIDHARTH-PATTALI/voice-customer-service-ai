from config import PDF_PATH
from voice_utils import listen, speak
from document_utils import load_vectorstore
from ai_utils import get_llm, ask_ai_question
import os

def main():
    print("🤖 AI Customer Service Assistant")

    if not os.path.exists(PDF_PATH):
        print(f"❌ PDF not found at: {PDF_PATH}")
        speak("The document was not found.")
        return

    vectorstore = load_vectorstore(PDF_PATH)
    retriever = vectorstore.as_retriever()
    llm = get_llm()

    while True:
        print("\n🎤 Ask a question (or say 'exit' to quit):")
        user_question = listen()
        if not user_question:
            continue
        if "exit" in user_question.lower():
            speak("Goodbye! Have a nice day ")
            print("👋 Exiting.")
            break
        ask_ai_question(llm, retriever, user_question)

if __name__ == "__main__":
    main()
