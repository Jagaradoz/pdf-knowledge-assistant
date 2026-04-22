from langchain_core.prompts import PromptTemplate
from main.config import LLM_BACKEND, OLLAMA_MODEL, OPENAI_API_KEY

class LLMGenerator:
    def __init__(self):
        """
        Initializes the LLM Backend based on config.py.
        """
        if LLM_BACKEND == "openai":
            # Requires langchain-openai package
            try:
                from langchain_openai import ChatOpenAI
            except ImportError:
                raise ImportError("Please install langchain-openai to use the OpenAI backend.")
                
            if not OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY is not set in config or environment.")
                
            self.llm = ChatOpenAI(temperature=0, api_key=OPENAI_API_KEY)
        else:
            # Default to Ollama
            from langchain_community.llms import Ollama
            self.llm = Ollama(model=OLLAMA_MODEL)
            
        # Define the prompt template from the Data Pipeline doc
        template = """You are a helpful AI assistant. Use the following pieces of retrieved context to answer the user's question. 
If you don't know the answer based on the context, just say that you don't know. Do not make up information.

--- CONTEXT ---
{context}
---------------

User Question: {query}
Answer:"""
        self.prompt = PromptTemplate(
            template=template,
            input_variables=["context", "query"]
        )

        # Create the generation chain
        self.chain = self.prompt | self.llm

    def generate_answer(self, context: str, query: str) -> str:
        """
        Generates an answer from the LLM given the context and query.
        """
        return self.chain.invoke({
            "context": context,
            "query": query
        })
