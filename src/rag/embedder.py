from langchain_huggingface import HuggingFaceEmbeddings

# Initialize the model once when the module is loaded.
# all-MiniLM-L6-v2 is a fast, lightweight local model suitable for our needs.
MODEL_NAME = 'all-MiniLM-L6-v2'

def get_embeddings_model() -> HuggingFaceEmbeddings:
    """
    Returns a configured LangChain HuggingFaceEmbeddings instance.
    """
    return HuggingFaceEmbeddings(model_name=MODEL_NAME)
