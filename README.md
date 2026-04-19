# RAG Chatbot using LangChain, Groq, ChromaDB, FastAPI, and Streamlit

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on custom documents.

Instead of relying only on the LLM’s knowledge, the system retrieves relevant information from a vector database and uses it as context to generate accurate responses.

The goal is to reduce hallucinations and provide grounded, document-based answers.

---

## Architecture

```
User (Streamlit UI)
        ↓
FastAPI (Backend API)
        ↓
LangChain (Orchestration)
        ↓
Retriever (ChromaDB)
        ↓
LLM (Groq - Mixtral)
        ↓
Response → UI
```

---

## Tech Stack

* **Frontend**: Streamlit
* **Backend**: FastAPI
* **LLM**: Groq (llama-70b)
* **Framework**: LangChain
* **Vector Database**: ChromaDB
* **Embeddings**: Hugging Face (sentence-transformers)

---

## Features

* Document-based question answering using RAG
* Fast inference using Groq API
* Modular architecture (UI, API, RAG pipeline separated)
* Persistent vector database using ChromaDB
* Supports PDF ingestion

---

## Project Structure

```
chatbot/
│
├── app.py              # Streamlit UI
├── main.py             # FastAPI backend
├── rag_pipeline.py     # RAG logic (retrieval + LLM)
├── ingest.py           # One-time document ingestion
├── requirements.txt
└── data/               # Input documents (PDFs)
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/pvnkm/RAG-chatbot.git
cd RAG-chatbot
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Set environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Update your code to read from environment variables:

```python
import os
groq_api_key = os.getenv("GROQ_API_KEY")
```

---

### 4. Add documents

Place your PDF files inside the `data/` folder.

---

### 5. Run ingestion (one-time step)

```
python ingest.py
```

This will:

* Load documents
* Split into chunks
* Generate embeddings
* Store in ChromaDB

---

### 6. Start FastAPI server

```
uvicorn main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### 7. Run Streamlit UI

```
streamlit run app.py
```

---

## How It Works

1. Documents are ingested and stored as embeddings in ChromaDB
2. User submits a query through the UI
3. FastAPI receives the request
4. LangChain retrieves relevant document chunks
5. Groq LLM generates an answer using retrieved context
6. Response is displayed in Streamlit

---

## Limitations

* Static document ingestion (no runtime uploads)
* No conversation memory
* No source citation in responses
* Basic prompt control

---

## Future Improvements

* Dynamic file upload (runtime ingestion)
* Chat memory (multi-turn conversations)
* Source attribution for answers
* Streaming responses
* Deployment (AWS / Docker)

---

## Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Vector search using embeddings
* Prompt-based control of LLM output
* Backend-frontend separation
* API-driven architecture

---

## License

This project is for learning and demonstration purposes.
