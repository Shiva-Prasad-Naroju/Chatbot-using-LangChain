import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Stop execution if key is missing
if groq_api_key is None:
    st.error("❌ GROQ_API_KEY is missing. Please check your .env file or Streamlit secrets.")
    st.stop()

# Set Groq API key
os.environ["GROQ_API_KEY"] = groq_api_key

# Streamlit UI
st.title("Celebrity search results")
input_text = st.text_input("Search the topic")

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about the celebrity {name}."
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="Provide only the full date of birth (DOB) of {person} in YYYY-MM-DD format. Do not include any extra text."
)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major world events that happened in the year {dob}."
)

# GROQ LLM
llm = ChatGroq(temperature=0.8, model_name="llama3-8b-8192")

# Memory Buffers
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')

# LLM Chains
chain1 = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=descr_memory)

# Combine chains
parent_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'description'],
    verbose=True
)

# Run the app
if input_text:
    result = parent_chain({'name': input_text})
    st.write(result)

    with st.expander('Person name'):
        st.info(person_memory.buffer)

    with st.expander('Major events'):
        st.info(descr_memory.buffer)
