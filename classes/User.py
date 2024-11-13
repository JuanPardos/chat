from core import Request
import hashlib

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def signUp(self):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        return Request.newUser(self.name, self.password)

    def login(self):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        return Request.login(self.name, self.password)