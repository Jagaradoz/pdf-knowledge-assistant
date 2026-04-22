from .retriever import VectorRetriever
from .generator import LLMGenerator
from src.core.logger import logger

class RAGPipeline:
    def __init__(self):
        """
        Initializes the RAG Pipeline with a retriever and a generator.
        """
        self.retriever = VectorRetriever()
        self.generator = LLMGenerator()
        logger.info("RAG Pipeline initialized.")

    def answer_query(self, query_text: str, n_results: int = 5) -> dict:
        """
        Processes a user query through the RAG flow:
        1. Retrieve relevant context
        2. Generate answer using LLM
        
        Returns a dictionary with the answer and source documents.
        """
        logger.info(f"Answering query: {query_text}")
        
        # 1. Retrieval
        search_results = self.retriever.query(query_text, n_results=n_results)
        
        if not search_results:
            logger.warning("No context found for the query.")
            return {
                "answer": "I'm sorry, but I couldn't find any relevant information in the documents to answer your question.",
                "sources": []
            }
            
        # Format context for the generator
        context = "\n\n".join([doc.page_content for doc, score in search_results])
        sources = [
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            } for doc, score in search_results
        ]
        
        # 2. Generation
        answer = self.generator.generate_answer(context, query_text)
        
        return {
            "answer": answer,
            "sources": sources
        }

# Singleton instance
rag_pipeline = RAGPipeline()
