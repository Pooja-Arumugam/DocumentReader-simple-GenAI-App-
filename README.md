# 📄 DocumentReader - Simple GenAI App (Single-File Version)

A minimal Generative AI-powered document reader built with **Streamlit**, **LangChain**, and **Ollama** using only a single Python script (`app.py`). Upload a document, ask any question about its content, and get instant, context-aware responses powered by LLaMA 3.

---

## 🚀 Features

- 📄 Upload `.txt`, `.pdf`, `.docx`, or `.csv` files
- 🤖 Ask natural language questions based on document content
- 🧠 Uses Retrieval-Augmented Generation (RAG) with LangChain
- 🦙 Powered by a local Ollama LLM (e.g. `llama3`)
- ⚡ Single-file Python app for fast setup and demo

---

## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [FAISS](https://github.com/facebookresearch/faiss) (via LangChain)
- PDF/Doc/CSV parsers: `PyPDF2`, `docx2txt`, `pandas`

---

## 📦 Installation

### 1. Clone the Repository

```
git clone https://github.com/Pooja-Arumugam/DocumentReader-simple-GenAI-App-.git
cd DocumentReader-simple-GenAI-App-

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Requirements
```
pip install -r requirements.txt

### 4. Setup Environment Variables
```
Create a .env file in the project root:
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=DocumentReader

### 5. Download Ollama Model
```
Make sure you have Ollama installed and running:
ollama run llama3
