from core import request

class Message:
    def __init__(self, chat, sender, text, hash, timestamp):
        self.chat = chat
        self.sender = sender
        self.text = text
        self.hash = hash
        self.timestamp = timestamp
    
    def new(self):
        return request.newMessage(self.chat, self.sender, self.text)