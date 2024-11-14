from utils import apiResponse
from utils import crypto
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
        response = requests.post(url, data=crypto.encryptChacha20(user, data))
        return apiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 409:
            return "User already exists"
        
def newChat(user1, user2):
    url = endpoint + "newChat"
    data = {"user1": user1, "user2": user2}
    try:
        response = requests.post(url, data=crypto.encryptChacha20(user1, data))
        return apiResponse.parseChat(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 409:
            return "Chat already exists"

def newMessage(chat, sender, text):
    url = endpoint + "newMessage"
    data = {"chat": chat, "sender": sender, "text": text}
    try:
        response = requests.post(url, data=crypto.encryptChacha20(sender, data))
        return apiResponse.parseMessage(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "Chat not found"


def login(user, password):
    url = endpoint + "login"
    data = {"user": user, "password": password}
    try:
        response = requests.post(url, data=crypto.encryptChacha20(user, data))
        return apiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            return "Invalid credentials"

def getOnlineUsers():
    url = endpoint + "getOnlineUsers"
    try:
        response = requests.post(url, data = None)
        return apiResponse.parseUsers(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    
def getChatByUsers(user1, user2):
    url = endpoint + "getChatByUsers"
    data = {"user1": user1, "user2": user2}
    try:
        response = requests.post(url, data=crypto.encryptChacha20(user1, data))
        return apiResponse.parseChat(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "Chat not found"
        
def getUserByName(username):
    url = endpoint + "getUserByName"
    data = {"username": username}
    try:
        response = requests.post(url, data=crypto.encryptChacha20(username, data))
        return apiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "User not found"

def keyExchange(user, public_key):
    url = endpoint + "keyExchange"
    data = {"user": user, "public_key": public_key}
    try:
        response = requests.post(url, data=data)
        return response.json()
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 500:
            return "Internal server error"