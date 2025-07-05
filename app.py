# app.py
import streamlit as st
import uuid
from mcp import MCPBus, MCPMessage
from agents_and_utils import IngestionAgent, RetrievalAgent, LLMResponseAgent

st.set_page_config(page_title="📚 Agentic RAG Chatbot with Continuous Chat")
st.title("📚 Agentic RAG Chatbot using MCP (Ollama Edition)")

model = st.selectbox("Choose Ollama Model", ["llama3", "phi3", "mistral"])
uploaded_files = st.file_uploader("Upload Documents (PDF, DOCX, CSV, TXT, PPTX)", accept_multiple_files=True)

if "vector_store_initialized" not in st.session_state:
    st.session_state.vector_store_initialized = False
    st.session_state.chat_history = []
    st.session_state.llm = None

if uploaded_files and not st.session_state.vector_store_initialized:
    with st.spinner("📚 Parsing and embedding documents (please wait)..."):
        bus = MCPBus()
        ingest = IngestionAgent(bus)
        retrieve = RetrievalAgent(bus)
        st.session_state.llm = LLMResponseAgent(bus, model)

        trace_id = str(uuid.uuid4())
        bus.send(MCPMessage("UI", "IngestionAgent", "START", trace_id, {"files": uploaded_files, "query": "init"}))

        st.session_state.vector_store_initialized = True
        st.success("✅ Documents uploaded and processed!")

if st.session_state.vector_store_initialized:
    query = st.text_input("💬 Ask a question about the uploaded documents:")
    if st.button("Ask") and query:
        with st.spinner("🤖 Generating response..."):
            bus = MCPBus()
            RetrievalAgent(bus)
            bus.register("LLMResponseAgent", st.session_state.llm.handle)

            trace_id = str(uuid.uuid4())
            bus.send(MCPMessage("UI", "RetrievalAgent", "ASK", trace_id, {"query": query}))

            answer = st.session_state.llm.final_answer
            st.session_state.chat_history.append((query, answer))

    for q, a in st.session_state.chat_history:
        st.markdown(f"**You**: {q}")
        st.markdown(f"**Bot**: {a}")
