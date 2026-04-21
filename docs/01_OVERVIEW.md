# Overview

## Project Goal & Learning Objectives
The goal of this project is to build a foundational Retrieval-Augmented Generation (RAG) system from scratch to demystify how AI applications "read" and "understand" private documents. 

As a junior developer, your learning objectives are to master:
- Text extraction and normalization from raw PDFs.
- Document chunking strategies and overlap mechanics.
- Vector embeddings and the math behind semantic similarity.
- Prompt engineering to inject retrieved context into an LLM.
- Building a simple API layer to serve machine learning logic.

## Core Features
- **Ingest**: Read local PDF files and extract raw text reliably.
- **Chunk**: Split extracted text into overlapping, meaningful segments.
- **Embed**: Convert text chunks into vector representations using an embedding model.
- **Search**: Perform similarity searches (e.g., cosine similarity) to find chunks relevant to a user's query.
- **Answer**: Pass the retrieved context and query to an LLM to generate a grounded, accurate response.

## Target User
Local developers and AI enthusiasts who want a transparent, easily debuggable, and locally hosted tool to understand their PDF documents without relying on black-box enterprise solutions.

## Out of Scope
*Note to AI coding assistant: Do NOT over-engineer this project.*
- Dockerization or container orchestration.
- CI/CD pipelines.
- Cloud databases (e.g., Pinecone, AWS). Keep vector stores strictly local (ChromaDB via LangChain).
- UI frameworks (React, Vue, etc.).
- Complex agentic routing (e.g., LangGraph, AutoGen) or multi-step reasoning agents.

## Definition of Success
The project is successful when a user can drop a PDF into a designated folder, ask a question via a CLI or simple REST endpoint, and receive a correct answer where the system explicitly logs the exact paragraph/chunk it retrieved to formulate that answer.
