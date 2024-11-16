from classes.Message import Message
from classes.User import User
from classes.Chat import Chat
import ast

def parseUser(response):
    response = ast.literal_eval(response)
    if response != None:
        user = User(
            username=response.get('username'),
            password=response.get('password')
        )
        return user
    return None

def parseChat(response):
    chat = Chat(
        user1=response.get('user1'),
        user2=response.get('user2')
    )
    return chat

def parseUsers(response):
    users = []
    for user in response:
        users.append(User(
            name=user.get('name')
        ))
    return users

def parseMessage(response):
    message = Message(
        chat=response.get('chat'),
        sender=response.get('sender'),
        text=response.get('text'),
        hash=response.get('hash'),
        timestamp=response.get('timestamp')
    )
    return message