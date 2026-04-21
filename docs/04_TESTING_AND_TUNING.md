# Testing and Tuning

## Sanity Checks
To ensure the system is learning rather than acting as a black box, implement these transparency checks during development:
- **Print Similarity Scores**: Always log the distance/similarity metric of your retrieved chunks. If the distance is too high (or score too low), it means the retriever is pulling irrelevant data.
- **Context Inspection**: Before sending the prompt to the LLM, print the exact `{context}` string to the terminal. If the context doesn't contain the answer, the LLM will fail (or hallucinate). Fix the retriever first, not the LLM.

## Tuning Knobs
Experiment with these variables to see how they affect RAG performance:
- **Chunk Size**: Try 200 characters vs. 1000 characters. Smaller chunks provide precise context but might lose the surrounding narrative. Larger chunks retain context but consume more tokens and might dilute the specific answer.
- **Chunk Overlap**: Try 0 overlap vs. 200 overlap. Notice how 0 overlap might split a crucial sentence in half, causing the retriever to miss it.
- **Top-K Retrieval**: Change how many chunks are retrieved (e.g., top 1 vs. top 5). See how adding more chunks increases context but also increases the risk of confusing the LLM with conflicting information.

## Edge Cases to Handle
- **Scanned/Empty PDFs**: Implement a check in the parser. If the extracted text length is 0, raise a clear error indicating the PDF might be an image/scan requiring OCR (which is out of scope).
- **Irrelevant Queries**: Test what happens when you ask "What is the recipe for cake?" against a financial PDF. Ensure your prompt instruction ("If you don't know the answer... say that you don't know") is strictly followed.
- **Vector Store Persistence**: Ensure that restarting the application doesn't require re-embedding the entire PDF. The system should load the existing index from disk on startup.