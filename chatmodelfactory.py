import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI, ChatOllama


load_dotenv()

def openai_chatmodel(model : str):
    """instantiates and returns an openai chat model

    Args:
        model (str): The openai model to use. eg: gpt-3.5-turbo-1106, gpt-4-1106-preview, gpt-4-32k, gpt-4

    Returns:
        ChatOpenAI: The langchain Chat model
    """
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    return ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=model)

def ollama_chatmodel(model: str):
    """Instantiates and returns an openai chat model.
    Note: The model must already be pulled inn Ollama.

    Args:
        model (str): The Ollama model to use. eg: codellama:13b, vicuna:7b, llama2:7b, mistral

    Returns:
        ChatOllama: The langchain Chat model
    """
    OLLAMA_HOST = os.environ.get("OLLAMA_HOST")
    return ChatOllama(base_url=OLLAMA_HOST, model=model)

