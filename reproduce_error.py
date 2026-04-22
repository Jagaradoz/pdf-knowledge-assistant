try:
    from langchain_core.language_models.chat_models import LangSmithParams
    print("Successfully imported LangSmithParams from langchain_core.language_models.chat_models")
except ImportError as e:
    print(f"ImportError: {e}")

try:
    from langchain_openai import ChatOpenAI
    print("Successfully imported ChatOpenAI from langchain_openai")
except ImportError as e:
    print(f"ImportError in langchain_openai: {e}")
