import os
import streamlit as st
from langchain_groq import ChatGroq  #  Correct import for Groq
from langchain.schema import HumanMessage

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# Set Groq API key
os.environ["GROQ_API_KEY"] = groq_api_key

# Streamlit UI
st.title("LangChain Project with Groq API")
input_text = st.text_input("Search the topic")

# Initialize the LLM with Groq
llm = ChatGroq(temperature=0.8, model_name="llama3-8b-8192")

# Generate response
if input_text:
    response = llm([HumanMessage(content=input_text)])
    st.write(response.content)
