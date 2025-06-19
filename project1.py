import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Stop if key is missing
if groq_api_key is None:
    st.error("❌ GROQ_API_KEY is missing. Please check your .env file.")
    st.stop()

# Set Groq API key
os.environ["GROQ_API_KEY"] = groq_api_key

# Streamlit UI
st.set_page_config(page_title="LangChain Chat", page_icon="🤖", layout="centered")
st.title("LangChain Project with Groq API")

input_text = st.text_input("Search the topic")

# Initialize the LLM
llm = ChatGroq(temperature=0.8, model_name="llama3-8b-8192")

# Generate and display response
if input_text:
    response = llm([HumanMessage(content=input_text)])
    st.write(response.content)
