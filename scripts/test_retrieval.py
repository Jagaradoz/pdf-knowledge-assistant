import os
import sys

# Add the src directory to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from rag.retriever import VectorRetriever

def main():
    # Initialize the retriever
    retriever = VectorRetriever()
    
    # Check if we have items in the store
    count = retriever.get_collection_count()
    if count == 0:
        print("The vector store is empty. Please run 'python scripts/test_ingestion.py' first.")
        return

    print(f"--- Vector Store Status: {count} items indexed ---")
    
    # Get user query
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("\nEnter your search query: ")
    
    if not query.strip():
        print("Empty query. Exiting.")
        return

    print(f"\nSearching for: '{query}'...")
    
    try:
        # Perform retrieval
        results = retriever.query(query, n_results=3)
        
        # Display results
        documents = results['documents'][0]
        metadatas = results['metadatas'][0]
        distances = results['distances'][0]

        print("\n--- Top 3 Relevant Results ---")
        for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances)):
            source = meta.get('source', 'Unknown')
            print(f"\n[Result {i+1}] (Distance: {dist:.4f}) | Source: {source}")
            print("-" * 30)
            # Show first 300 chars of the chunk
            preview = doc.replace('\n', ' ')[:300]
            print(f"{preview}...")
            
    except Exception as e:
        print(f"\nRetrieval failed: {e}")

if __name__ == "__main__":
    main()
