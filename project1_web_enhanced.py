# This file is functionally same as main.py but includes a bit
# enhanced and visually appealing web interface.

import os
import streamlit as st
from constants import groq_api_key
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
import time

# Set Groq API key
os.environ["GROQ_API_KEY"] = groq_api_key

# Initialize the LLM with Groq
llm = ChatGroq(temperature=0.8, model_name="llama3-8b-8192")

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        padding: 1rem;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        margin-left: 20%;
        text-align: right;
    }
    .ai-message {
        background: #f1f3f4;
        color: #333;
        padding: 0.8rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        margin-right: 20%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Chat Assistant</h1>
    <p>Experience the power of advanced AI with beautiful, intuitive conversations</p>
</div>
""", unsafe_allow_html=True)

# Features section
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### ⚡ Lightning Fast")
    st.write("Get instant responses powered by Groq LLM")
with col2:
    st.markdown("### 🧠 Advanced AI")
    st.write("Complex problem-solving capabilities")
with col3:
    st.markdown("### 💬 Natural Conversations")
    st.write("Human-like conversation experience")

# Chat interface
st.markdown("### 💬 Chat Interface")

# Display chat history
if st.session_state.messages:
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f'<div class="user-message">👤 You: {message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="ai-message">🤖 AI: {message["content"]}</div>', unsafe_allow_html=True)

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_area("Ask me anything...", height=100, placeholder="Type your message here...")
    submitted = st.form_submit_button("Send Message", use_container_width=True)

if submitted and user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show loading spinner
    with st.spinner("AI is thinking..."):
        try:
            # Generate response
            response = llm([HumanMessage(content=user_input)])
            ai_response = response.content
            
            # Add AI response to history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    # Rerun to update the chat display
    st.rerun()

# Sidebar with additional info
with st.sidebar:
    st.markdown("### 🔧 Settings")
    st.write("**Model:** Llama 3 8B")
    st.write("**Temperature:** 0.8")
    st.write("**Provider:** Groq")
    
    st.markdown("### 📊 Statistics")
    st.write(f"**Messages:** {len(st.session_state.messages)}")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
