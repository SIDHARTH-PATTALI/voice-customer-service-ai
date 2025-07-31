from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader

def load_vectorstore(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(pages, embeddings)

    return vectorstore
