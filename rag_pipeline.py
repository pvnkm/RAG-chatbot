from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def get_qa_chain():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectordb = Chroma(embedding_function=embedding,persist_directory='db')

    retriever = vectordb.as_retriever()

    llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'),model="llama-3.3-70b-versatile",temperature=0.1)

    qa_chain = RetrievalQA.from_chain_type(llm=llm,retriever=retriever,chain_type="stuff")

    return qa_chain