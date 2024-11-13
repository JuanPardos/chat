from utils import ApiResponse
from env import dev
import requests

endpoint = dev.endpoint

if(endpoint == "http://endpoint:port/"):
    print("Please change the endpoint in env/dev.py")
    exit()

def newUser(user, password):
    url = endpoint + "newUser"
    data = {"user": user, "password": password}
    try:
        response = requests.post(url, data=data)
        return ApiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 409:
            return "User already exists"
        
def newChat(user1, user2):
    url = endpoint + "newChat"
    data = {"user1": user1, "user2": user2}
    try:
        response = requests.post(url, data=data)
        return ApiResponse.parseChat(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 409:
            return "Chat already exists"

def newMessage(chat, sender, text):
    url = endpoint + "newMessage"
    data = {"chat": chat, "sender": sender, "text": text}
    try:
        response = requests.post(url, data=data)
        return ApiResponse.parseMessage(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "Chat not found"


def login(user, password):
    url = endpoint + "login"
    data = {"user": user, "password": password}
    try:
        response = requests.post(url, data=data)
        return ApiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            return "Invalid credentials"

def getOnlineUsers():
    url = endpoint + "getOnlineUsers"
    try:
        response = requests.get(url)
        return ApiResponse.parseUsers(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    
def getChatByUsers(user1, user2):
    url = endpoint + "getChatByUsers/" + user1 + "/" + user2
    data = {"user1": user1, "user2": user2}
    try:
        response = requests.get(url)
        return ApiResponse.parseChat(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "Chat not found"
