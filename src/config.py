import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Select the LLM Backend: "ollama" or "openai"
# To change the backend, modify this variable or set the LLM_BACKEND environment variable.
LLM_BACKEND = os.getenv("LLM_BACKEND", "ollama").lower()

# Ollama settings
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

# OpenAI settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
