import os
from langchain_chroma import Chroma
from langchain_core.documents import Document
from rag.embedder import get_embeddings_model

# Define the path for the local ChromaDB store
DB_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'vector_store')
COLLECTION_NAME = "pdf_chunks"

class VectorRetriever:
    def __init__(self):
        # Initialize the LangChain Chroma vector store
        self.embedding_function = get_embeddings_model()
        self.vectorstore = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=self.embedding_function,
            persist_directory=DB_DIR
        )

    def add_documents(self, documents: list[Document]):
        """
        Adds LangChain Document objects to the vector store.
        """
        if not documents:
            return

        # Add to ChromaDB via LangChain
        self.vectorstore.add_documents(documents=documents)
        
    def get_collection_count(self) -> int:
        """
        Returns the number of items currently in the collection.
        """
        return len(self.vectorstore.get()['ids'])

    def query(self, query_text: str, n_results: int = 5) -> list[tuple[Document, float]]:
        """
        Searches for the most relevant documents based on the query text.
        Returns a list of tuples containing the Document and its similarity score.
        """
        # Query ChromaDB via LangChain
        results = self.vectorstore.similarity_search_with_score(
            query=query_text,
            k=n_results
        )
        
        return results
