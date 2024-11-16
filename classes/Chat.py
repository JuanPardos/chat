from core import request

class Chat:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
    
    def new(self):
        return request.newChat(self.user1, self.user2)
    
    def get(self):
        return request.getChatByUsers(self.user1, self.user2)