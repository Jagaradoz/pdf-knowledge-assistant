import os
import chromadb
import uuid

# Add src to sys.path is not needed here as it will be imported from scripts/main
from rag.embedder import get_embeddings

# Define the path for the local ChromaDB store
DB_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'vector_store')
COLLECTION_NAME = "pdf_chunks"

class VectorRetriever:
    def __init__(self):
        # Initialize the persistent ChromaDB client pointing to our data directory
        self.client = chromadb.PersistentClient(path=DB_DIR)
        
        # Get or create a collection. We use cosine similarity for text search.
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"hnsw:space": "cosine"}
        )

    def add_chunks(self, chunks: list[str], metadatas: list[dict] = None):
        """
        Generates embeddings for the chunks and adds them to the vector store.
        """
        if not chunks:
            return

        # Generate unique IDs for each chunk
        ids = [str(uuid.uuid4()) for _ in chunks]
        
        # Generate embeddings using our local embedder
        embeddings = get_embeddings(chunks)
        
        # If no metadatas provided, create empty dicts
        if metadatas is None:
            metadatas = [{} for _ in chunks]
            
        # Add to ChromaDB
        self.collection.add(
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )
        
    def get_collection_count(self) -> int:
        """
        Returns the number of items currently in the collection.
        """
        return self.collection.count()
