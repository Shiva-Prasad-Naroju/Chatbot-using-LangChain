# 🤖 AI Projects Using LangChain + Groq + Streamlit

Welcome to my AI projects built using **LangChain**, **Groq’s LLaMA3 models**, and **Streamlit**. These projects demonstrate the power of large language models through conversational interfaces and intelligent reasoning using chaining techniques.

## 📌 Overview

This repository contains **two major projects**:

### 🔹 Project 1: Language Model Chatbot

- `project1.py` – A basic LLM-powered chatbot using **Groq** and **Streamlit**.

    project1 webpage: https://chatbot-using-langchain-qujjac9mfny2ruzbjqjmhg.streamlit.app/

- `project1_web_enhanced.py` – Functionally the same as project1 , but with a **visually enhanced UI** using custom CSS (dark theme, carousels, and improved layout).

    project1_web_enhanced webpage: https://shiva-prasad-naroju-chatbot-using--project1-web-enhanced-nfbuce.streamlit.app/

### 🔹 Project 2: Chained Prompt AI System

- `project2.py` – An intelligent agent built using **LangChain’s chaining** capabilities and **prompt templates**.

  - Input: Celebrity name
    
  - Output:
    
  - ## 🧠 Chain Flow:
 
    1. Description of the celebrity
    2. Their date of birth (DOB)
    3. 5 major world events from their birth year

    project2.py web link: https://shiva-prasad-naroju-chatbot-using-langchain-project2-wfsl74.streamlit.app/

    Used 3 chained LLMChains wrapped in a SequentialChain. Each output is passed as input to the next step.


This is my **first LangChain project** using chaining, memory, and structured prompt engineering.

## 🔧 Technologies Used

| Tool                    | Purpose                                           |
|-------------------------|---------------------------------------------------|
| 🧠 LangChain            | Chaining LLMs, prompt templates, memory           |
| ⚡ Groq API             | Backend LLM provider (LLaMA3-8B model)            |
| 🌐 Streamlit            | Web application UI                                |
| 🔗 PromptTemplate       | Controlled prompt design                          |
| 🧠 ConversationBufferMemory | Retains context across chains                  |
| 🎨 Custom CSS (in UI version) | Visual enhancements (dark theme, cards)     |

## 📁 Project Structure

├── project1.py # Basic (search application) chatbot using Groq API

├── project1_web_enhanced.py # UI-enhanced chatbot with Streamlit + CSS

├── project2.py # LangChain project using chained prompts for celebrity search

├── .env # Stores API key (groq_api_key=xxxxxxx)

├── requirements.txt # Python dependencies

├── .gitignore # Prevents pushing secrets and environments

