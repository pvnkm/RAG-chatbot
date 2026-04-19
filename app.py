import streamlit as st
import requests

st.title('RAG Chatbot')

user_input = st.text_input("Ask Something: ")

if st.button('send'):
    res = requests.post("http://127.0.0.1:8000/chat", json={"question":user_input})

    if res.status_code == 200:
        st.write(res.json()["answer"])
