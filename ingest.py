from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

##Load PDF
loader = PyPDFLoader('D:\Pavan\Projects\GenAI_Projects\Q&A_Chatbot\data\GenAI_Interview_Questions.pdf')
documents = loader.load()

#Split
splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=10)
docs = splitter.split_documents(documents=documents)
print(docs)

#Embedding
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#store in chroma
vectordb = Chroma.from_documents(docs,embedding,persist_directory='db')

print("Data Ingested Successfully!")

