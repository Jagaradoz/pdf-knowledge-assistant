import sys
import os

# Ensure src is in the python path (parent of main directory)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.retriever import VectorRetriever
from rag.generator import LLMGenerator

def main():
    print("Initializing RAG System...")
    try:
        retriever = VectorRetriever()
        generator = LLMGenerator()
    except Exception as e:
        print(f"Error initializing system: {e}")
        return

    print("RAG System Ready! Type 'exit' or 'quit' to stop.")
    print("-" * 40)
    
    while True:
        try:
            query = input("\nUser: ").strip()
            if query.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            if not query:
                continue
                
            print("\nSearching for context...")
            # 1. Retrieve relevant chunks
            results = retriever.query(query, n_results=3)
            
            if not results:
                print("No relevant context found in the database. Are you sure you ingested documents?")
                continue
                
            # Construct the context string
            context_pieces = []
            print("\n--- Retrieved Source Chunks ---")
            for i, (doc, score) in enumerate(results):
                # Using distance score (lower is better for L2, higher is better for cosine depending on implementation)
                print(f"[Chunk {i+1} | Score: {score:.4f}]: {doc.page_content[:150]}...")
                context_pieces.append(doc.page_content)
            print("-------------------------------\n")
            
            context_str = "\n\n".join(context_pieces)
            
            # 2. Generate Answer
            print("Assistant is thinking...")
            answer = generator.generate_answer(context=context_str, query=query)
            
            print("\nAssistant:")
            print(answer)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
