from langchain.chat_models.base import BaseChatModel
from git import Repo
from langchain.memory.entity import SQLiteEntityStore
from langchain.chains import ConversationalRetrievalChain, ConversationChain
from langchain.chains.conversational_retrieval.base import BaseConversationalRetrievalChain

class chatbot:
    chatmodel: BaseChatModel = None

    def __init__(self):
        SQLiteEntityStore()
        ConversationalRetrievalChain.from_llm()
