from ..utils.messageUtil import MessageUtil
from .llmService import LLMService

class MessageService:

    def __init__(self):
        self.messageUtil = MessageUtil()
        self.llmService = LLMService()

    def processMessage(self , message):
        if self.messageUtil.isBankMessage(message):
            return self.llmService.runLLM(message)
        else:
            return None