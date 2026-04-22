# Data Pipeline

## RAG Pipeline Flow
1. **Document Processing (Vectorization)**: 
   - **PDF -> Text**: Extract raw strings using `pdfplumber`.
   - **Text -> Chunks**: Split into overlapping 1000-character segments.
   - **Chunks -> Vectors**: Convert to high-dimensional arrays using `sentence-transformers`.
   - **Vectors -> Store**: Save to a local ChromaDB index.
2. **Retrieval**:
   - **Query -> Search**: Embed the user's query and perform a similarity search in ChromaDB to find relevant chunks.
3. **Generation**:
   - **Search -> Prompt**: Inject retrieved context into an LLM prompt.
   - **Prompt -> LLM**: Generate a synthesized answer grounded in the context.

## Folder Structure
```text
pdf-knowledge-assistant/
├── data/
│   ├── raw/                 # PDF source files
│   └── vector_store/        # Local ChromaDB files
├── src/
│   ├── ingest/
│   │   ├── parser.py        # Extraction logic
│   │   ├── chunker.py       # Splitting logic
│   │   └── processor.py     # Unified ingestion orchestration
│   ├── rag/
│   │   ├── embedder.py      # Embedding generation
│   │   └── retriever.py     # Search and storage logic
│   ├── api/
│   │   └── main.py          # FastAPI application
│   └── main/
│       ├── cli.py           # Main CLI entrypoint
│       └── config.py        # Environment settings
├── scripts/               # Utility scripts (dataset generation, etc.)
├── notebooks/             # Self-contained educational sandboxes for each phase
├── docs/                    # Project documentation
├── requirements.txt
└── .env                     # Configuration
```

## Component Responsibilities
- **Processor (`processor.py`)**: The central entry point for document ingestion. Orchestrates parsing, chunking, and storage.
- **Parser (`parser.py`)**: Handles PDF reading and text extraction via `PDFPlumberLoader`.
- **Chunker (`chunker.py`)**: Implements document splitting via `RecursiveCharacterTextSplitter`.
- **Retriever (`retriever.py`)**: Manages the local vector database and performs similarity searches.
- **Embedder (`embedder.py`)**: Houses the embedding model and logic.

## Prompt Design
The retrieved context must be cleanly separated from the user's instructions:
```text
You are a helpful AI assistant. Use the following pieces of retrieved context to answer the user's question. 
If you don't know the answer based on the context, just say that you don't know. Do not make up information.

--- CONTEXT ---
{context}
---------------

User Question: {query}
Answer:
```