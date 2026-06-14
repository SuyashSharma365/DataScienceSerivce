from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI

from langchain_core.utils.function_calling import convert_to_openai_tool
from dotenv import load_dotenv , dotenv_values
import os
from .Expense import Expense

class LLMService:
    def __init__(self):
        load_dotenv()
        self.promt = ChatPromptTemplate.from_messages([
                (
                    "system",

                    """
                    You are an expert extaction alogrithm.
                    Only extract the relevant information from the message.
                    If you know the value of an attribute asked to extract.
                    return null for the attribute's value.
                    """
                ),
                ("human", "{text}")

            ]
        )
        self.apiKey = os.getenv("MISTRAL_API_KEY")
        self.llm = ChatMistralAI(api_key=self.apiKey, model="mistral-large-latest")
        self.runnable = self.promt | self.llm.with_structured_output(schema=Expense)

    def runLLM(self , message):
        return self.runnable.invoke({"text": message})