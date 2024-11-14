from classes import User, Chat, Message

def parseUser(response):
    user = User(
        name=response.get('name')
    )
    return user

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