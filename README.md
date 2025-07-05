# 📚 Agentic RAG Chatbot using MCP (Ollama Edition)

This project is a **local, private, document-based chatbot** built using the **Model Context Protocol (MCP)** with **agentic architecture**. It uses `Ollama` for running local LLMs like `llama3` and lets users upload PDF, DOCX, CSV, TXT, and PPTX files to query them in natural language.

## 🧠 Project Features

- 🔍 Retrieval-Augmented Generation (RAG) with FAISS and Ollama
- 🤖 Agent-based flow: Ingestion, Retrieval, and LLM Response Agents
- 📂 Supports multi-format file uploads (.pdf, .docx, .txt, .csv, .pptx)
- 🧠 Embedding via MiniLM transformer
- ⚙️ Local LLM inference using Ollama
- 🖥️ User-friendly Streamlit interface

## 🎥 Video Demo

📺 https://www.loom.com/share/0c4146e2f75c4d22b752408b3c63e409

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/your-username/agentic-rag-ollama
cd agentic-rag-ollama
```

### 2. Create Environment & Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate   # Use 'source venv/bin/activate' for Linux/macOS
pip install -r requirements.txt
```

### 3. Start Ollama and Pull Model
```bash
ollama pull llama3
ollama run llama3
```

### 4. Launch the App
```bash
streamlit run app.py
```

## 🧩 Architecture

```
User ↔ Streamlit UI ↔ MCP Bus
      ├── IngestionAgent → Parse docs + Embed chunks → Store in FAISS
      ├── RetrievalAgent → Embed query → Search FAISS → Top Chunks
      └── LLMResponseAgent → Use Ollama to answer with context
```

## 📂 Project Structure

```
📁 agentic-rag-ollama
├── app.py               # Main Streamlit UI
├── mcp.py               # Message passing protocol
├── agents_and_utils.py  # All agent classes + FAISS logic
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## ✅ Dependencies

- streamlit  
- faiss-cpu  
- sentence-transformers  
- PyMuPDF (fitz)  
- python-docx  
- python-pptx  
- ollama  

Install them using:
```bash
pip install -r requirements.txt
```

## 👤 Author

**Vishnu**  
Agentic RAG + Ollama + Streamlit Project powered by LLMs 🔍🤖📄
