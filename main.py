from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import get_qa_chain

app = FastAPI()

qa_chain = get_qa_chain()

class Query(BaseModel):
    question: str

@app.post('/chat')
def chat(query: Query):
    response = qa_chain.invoke(query.question)
    return {"answer": response}