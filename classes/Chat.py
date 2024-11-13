from core import Request

class Chat:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
    
    def new(self):
        return Request.newChat(self.user1, self.user2)
    
    def get(self):
        return Request.getChatByUsers(self.user1, self.user2)