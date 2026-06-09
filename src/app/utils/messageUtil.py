import re

class MessageUtil:

    def isBankMessage(self , message):
        word_list = ['bank' ,'card','bank']
        pattern = r'\b(?:' + '|'.join(re.escape(word) for word in word_list) + r')\b'
        return bool(re.search(pattern, message , re.IGNORECASE))