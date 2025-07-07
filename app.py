import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#  environment variable name
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

#  LangChain prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.set_page_config(page_title="LangChain + Ollama Demo", layout="centered")
st.title("🧠 LangChain Demo with LLaMA3 2.1B")
st.markdown("Ask anything and get a smart response from a local model using **LangChain + Ollama**.")

# User Input
input_text = st.text_input("🔎 What’s your question?", key="user_input")

# Convert to lowercase (auto-correct caps lock)
if input_text:
    normalized_input = input_text.lower().strip()
    
    with st.spinner("🤖 Thinking..."):
        # Setup chain
        llm = Ollama(model="llama3.2:1b")
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        try:
            response = chain.invoke({"question": normalized_input})
            st.success("✅ Answer:")
            st.markdown(f"```\n{response.strip()}\n```")
        except Exception as e:
            st.error(f"⚠️ Error generating response: {e}")
else:
    st.info("💡 Tip: Enter your question above and press Enter.")
