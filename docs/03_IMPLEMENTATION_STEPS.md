# Implementation Steps

## Phase 1: Document Processing and Vectorization (LangChain Edition)
- **Task 1**: Create `src/ingest/parser.py`. Use LangChain's `PDFPlumberLoader` to read a sample PDF from `data/raw/` and extract `Document` objects.
- **Task 2**: Create `src/ingest/chunker.py`. Use LangChain's `RecursiveCharacterTextSplitter` on the `Document`s.
- **Task 3**: Create `src/rag/embedder.py` to initialize your local embedding model (`HuggingFaceEmbeddings`).
- **Task 4**: Create `src/rag/retriever.py`. Initialize a local LangChain `Chroma` vector store in `data/vector_store/`.
- **Task 5**: Create `src/ingest/processor.py`. Orchestrate the flow: PDF -> Documents -> Chunks -> Embeddings -> Vector Store.
- **Task 6 (Educational)**: Create `notebooks/01_document_vectorization.ipynb` to verify and visualize each step interactively.
- **Definition of Done**: Running `scripts/test_ingestion.py` successfully extracts text, chunks it, embeds it, and saves it to the local vector store.

## Phase 2: The Retrieval Search
- **Task 1**: Update `retriever.py` with a `search(query: str, top_k: int = 3)` method.
- **Task 2**: Embed the incoming query string using the embedder.
- **Task 3**: Query the vector store and return the exact text of the top 3 matches along with their similarity scores.
- **Task 4 (Educational)**: Create `notebooks/02_retrieval_and_search.ipynb` to experiment with different `top_k` values and search distances.
- **Definition of Done**: Running a hardcoded query in a test script prints out the 3 most relevant paragraphs and their similarity scores.

## Phase 3: LLM Integration & CLI
- **Task 1**: Create `src/cli.py`.
- **Task 2**: Setup the LLM client (OpenAI or local).
- **Task 3**: Implement the prompt template defined in the Data Pipeline doc.
- **Task 4**: Create a continuous `while True:` loop in `cli.py`.
- **Task 5 (Educational)**: Create `notebooks/03_llm_integration.ipynb` to test prompt variations and judge answer quality.
- **Definition of Done**: A fully functional terminal chatbot that answers questions based on the ingested PDF and explicitly shows which chunks it used.

## Phase 4: FastAPI Wrapper
- **Task 1**: Create `src/api/main.py`. Initialize a FastAPI app.
- **Task 2**: Create a `POST /ingest` endpoint and a `POST /ask` endpoint.
- **Definition of Done**: You can successfully upload a PDF via Swagger UI and get accurate answers from the `/ask` endpoint.