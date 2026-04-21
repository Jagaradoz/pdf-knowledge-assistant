# PDF Knowledge Assistant

A local, educational Retrieval-Augmented Generation (RAG) system built to demystify how AI applications "read" and "understand" private documents. This project implements a full RAG pipeline—from raw PDF ingestion to semantic search and grounded answering.

## Features

- **Automated Dataset Generation**: Use the built-in scraper to fetch hundreds of high-quality research papers from arXiv for testing.
- **Modular RAG Pipeline**: Clear separation between ingestion (parsing/chunking), retrieval (embeddings/vector search), and the generation layer.
- **Local-First Architecture**: Built using local vector stores (FAISS) and local embedding models for privacy and cost-efficiency.
- **Transparent Logic**: Logs the exact chunks used to formulate every answer, making the AI's reasoning fully traceable.
- **Learning Sandbox**: Interactive Jupyter Notebooks for each phase to help you understand the "why" behind every line of code.

## Dataset Generation

This project includes a utility to quickly bootstrap a massive dataset of high-quality PDFs. To download 100+ research papers into your local environment:

```bash
python scripts/download_pdfs.py
```
*Note: This script hits the arXiv API and automatically organizes the papers into your data folder.*

## Tech Stack

| Technology | Role |
|------------|------|
| Python 3.10+ | Core development language |
| FastAPI | REST API framework for document queries |
| LangChain | Orchestration of text splitting and RAG logic |
| pdfplumber | Precise text extraction from complex PDF layouts |
| FAISS | High-performance local vector similarity search |
| sentence-transformers | Local semantic embeddings |
| OpenAI / Ollama | LLM providers for the final answering step |

## Project Structure

```text
pdf-knowledge-assistant/
├── src/
│   ├── api/               # FastAPI route handlers and server
│   ├── ingest/            # PDF extraction and segment chunking
│   ├── rag/               # Embedding logic and vector store management
│   ├── cli.py             # Terminal-based interactive chatbot
│   └── config.py          # Global environment settings
├── notebooks/             # Step-by-step educational experiments
├── .env.example           # Configuration template
├── .gitignore
├── scripts/               # Utility scripts (dataset generation, etc.)
│   ├── download_pdfs.py   # Massive PDF download utility
│   └── test_ingestion.py   # Ingestion testing script
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- (Optional) OpenAI API Key or local Ollama instance

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jagaradoz/pdf-knowledge-assistant.git
   cd pdf-knowledge-assistant
   ```

2. **Set up the environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Download your dataset:**
   ```bash
   python scripts/download_pdfs.py
   ```

4. **Start the assistant:**
   ```bash
   python src/cli.py
   ```

## Evaluation Flow

**Vectorize → Search → Answer**

1. **Vectorize**: PDF documents are extracted, chunked, embedded, and indexed into ChromaDB.
2. **Search**: User queries find the top-K most similar segments using semantic search.
3. **Answer**: Retrieved context is injected into an LLM prompt to generate a grounded response.
