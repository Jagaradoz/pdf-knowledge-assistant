from sentence_transformers import SentenceTransformer

# Initialize the model once when the module is loaded.
# all-MiniLM-L6-v2 is a fast, lightweight local model suitable for our needs.
MODEL_NAME = 'all-MiniLM-L6-v2'
model = SentenceTransformer(MODEL_NAME)

def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generates embeddings for a list of text chunks.
    """
    if not texts:
        return []
    
    # encode returns a numpy array, we convert it to a list of floats for chromadb
    embeddings = model.encode(texts)
    return embeddings.tolist()
