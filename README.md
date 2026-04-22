# PDF Knowledge Assistant

A local, educational Retrieval-Augmented Generation (RAG) system built to demystify how AI applications "read" and "understand" private documents. This project implements a full RAG pipeline—from raw PDF ingestion to semantic search and grounded answering.

## Features

- **Automated Dataset Generation**: Use the built-in scraper to fetch high-quality research papers from arXiv for testing.
- **Simplified RAG Architecture**: A flattened, easy-to-follow pipeline for embedding, retrieval, and generation.
- **Local-First Architecture**: Built using local vector stores (ChromaDB) and local embedding models for privacy and cost-efficiency.
- **Multi-Backend LLM Support**: Support for both OpenAI (API) and Ollama (Local) for the final answering step.
- **Educational Sandbox**: Interactive Jupyter Notebooks designed to help you understand the "why" behind every step of the RAG process.

## API Reference

### 1. Ask a Question
Submit a query to the RAG system to get an answer based on your documents.

**Endpoint**: `POST /api/query/`

**Request Body**:
```json
{
  "query": "What is CityRAG?",
  "llm_backend": "openai",
  "model": "gpt-4-turbo"
}
```

**Example (curl)**:
```bash
curl -X POST "http://localhost:8000/api/query/" \
     -H "Content-Type: application/json" \
     -d '{"query": "What is CityRAG?", "model": "gpt-4-turbo"}'
```

### 2. Health Check
Verify the system status.

**Endpoint**: `GET /api/system/health`

## Project Structure

```text
pdf-knowledge-assistant/
├── src/
│   ├── api/               # FastAPI route handlers, schemas, and dependencies
│   ├── core/              # Global configuration and logging
│   └── rag/               # Core RAG logic (Retriever, Generator, Pipeline)
├── notebooks/             # Step-by-step educational experiments
│   ├── 01_vectorization.ipynb
│   ├── 02_retrieval.ipynb
│   └── 03_llm_integration.ipynb
├── scripts/               # Utility scripts
│   ├── load_data.py       # Scrape ArXiv papers
│   └── ingest.py          # Process and index raw PDFs
├── data/                  # Local storage for PDFs and Vector DB
├── .env                   # Local environment settings
└── README.md
```

## Educational Flow

This project is organized into three distinct phases, mirroring the structure of the included notebooks:

1. **Phase 1: Vectorization**: PDF documents are extracted, chunked, and converted into semantic vectors using HuggingFace models.
2. **Phase 2: Retrieval**: User queries are transformed into vectors and compared against the database to find the most relevant document segments.
3. **Phase 3: Generation**: The retrieved segments are "stuffed" into a prompt template and sent to an LLM (OpenAI or Ollama) to generate a grounded answer.

## Getting Started

### 1. Installation

```bash
git clone https://github.com/Jagaradoz/pdf-knowledge-assistant.git
cd pdf-knowledge-assistant
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Prepare Your Data

Download a sample dataset of research papers:
```bash
python scripts/load_data.py
```

Process and index the PDFs into the vector database:
```bash
python scripts/ingest.py
```

### 3. Start the API

```bash
python -m uvicorn src.api.main:app --reload
```