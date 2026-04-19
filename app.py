import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("💬 RAG Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box 
if prompt := st.chat_input("Ask Something..."):
    
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to backend
    res = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"question": prompt}
    )

    if res.status_code == 200:
        
        # Show bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = res.json()["answer"]
        
                # Fix newline issue
                answer = answer.replace("\\n", "\n")

                st.markdown(answer)

        # Save response
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
    else:
        st.error("Error from backend")