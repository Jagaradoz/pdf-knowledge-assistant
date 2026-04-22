from langchain_core.prompts import PromptTemplate
from src.core.config import settings
from src.core.logger import logger

# Define the prompt template
PROMPT_TEMPLATE = """You are a helpful AI assistant. Use the following pieces of retrieved context to answer the user's question. 
If you don't know the answer based on the context, just say that you don't know. Do not make up information.

--- CONTEXT ---
{context}
---------------

User Question: {query}
Answer:"""

class LLMGenerator:
    def __init__(self):
        """
        Initializes the LLM Generator with lazy backend initialization.
        Both Ollama and OpenAI backends are created on first use.
        """
        self.prompt = PromptTemplate(
            template=PROMPT_TEMPLATE,
            input_variables=["context", "query"]
        )
        self._ollama_llm = None
        self._openai_llm = None

    def _get_ollama_llm(self):
        if self._ollama_llm is None:
            from langchain_community.llms import Ollama
            self._ollama_llm = Ollama(model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL)
            logger.info("Ollama LLM initialized.")
        return self._ollama_llm

    def _get_openai_llm(self):
        if self._openai_llm is None:
            try:
                from langchain_openai import ChatOpenAI
            except ImportError:
                raise ImportError("Please install langchain-openai to use the OpenAI backend.")
            if not settings.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY is not set in config or environment.")
            self._openai_llm = ChatOpenAI(temperature=0, api_key=settings.OPENAI_API_KEY)
            logger.info("OpenAI LLM initialized.")
        return self._openai_llm

    def _get_llm(self, llm_backend: str = None, model: str = None):
        backend = llm_backend or settings.LLM_BACKEND
        
        # If a specific model is requested, we create a temporary instance
        if model:
            if backend == "openai":
                from langchain_openai import ChatOpenAI
                return ChatOpenAI(model=model, temperature=0, api_key=settings.OPENAI_API_KEY)
            else:
                from langchain_community.llms import Ollama
                return Ollama(model=model, base_url=settings.OLLAMA_BASE_URL)
                
        # Otherwise use the cached default instances
        if backend == "openai":
            return self._get_openai_llm()
        return self._get_ollama_llm()

    def generate_answer(self, context: str, query: str, llm_backend: str = None, model: str = None) -> str:
        """
        Generates an answer from the LLM given the context and query.
        Optionally overrides the LLM backend or model for this request.
        """
        llm = self._get_llm(llm_backend, model)
        chain = self.prompt | llm
        return chain.invoke({
            "context": context,
            "query": query
        })
