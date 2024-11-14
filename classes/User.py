from core import request
import hashlib

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def new(self):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        return request.newUser(self.name, self.password)

    def login(self):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        return request.login(self.name, self.password)