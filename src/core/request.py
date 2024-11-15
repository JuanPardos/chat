from core import apiResponse, apiResponse
from utils import crypto
from env import dev
import requests

endpoint = dev.endpoint
headers = {'Content-Type': 'application/json'}

if(endpoint == "http://endpoint:port/"):
    print("Please change the endpoint in env/dev.py")
    exit()

def newUser(sessionKey, username, password):
    url = endpoint + "newUser"
    data = {"username": username, "password": password}    # Password is hashed in the backend
    try:
        response = requests.post(url, json=crypto.encryptData(sessionKey, data), headers=headers)
        return apiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 409:
            return "User already exists"
        
def newChat(sessionKey, user1, user2):
    url = endpoint + "newChat"
    data = {"user1": user1, "user2": user2}
    try:
        response = requests.post(url, json=crypto.encryptData(sessionKey, data), headers=headers)
        return apiResponse.parseChat(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 409:
            return "Chat already exists"

def newMessage(sessionKey, chat, sender, text):
    url = endpoint + "newMessage"
    data = {"chat": chat, "sender": sender, "text": text}
    try:
        response = requests.post(url, json=crypto.encryptData(sessionKey, data), headers=headers)
        return apiResponse.parseMessage(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "Chat not found"


def login(sessionKey, username, password):
    url = endpoint + "login"
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, json=crypto.encryptData(sessionKey, data), headers=headers)
        return apiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            return "Invalid credentials"

def getOnlineUsers(sessionKey):
    url = endpoint + "getOnlineUsers"
    try:
        response = requests.post(url, json=crypto.encryptData(sessionKey, data = None), headers=headers)
        return apiResponse.parseUsers(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    
def getChatByUsers(sessionKey, user1, user2):
    url = endpoint + "getChatByUsers"
    data = {"user1": user1, "user2": user2}
    try:
        response = requests.post(url, json=crypto.encryptData(sessionKey, data), headers=headers)
        return apiResponse.parseChat(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "Chat not found"
        
def getUserByName(sessionKey, username):
    url = endpoint + "getUserByName"
    data = {"username": username}
    try:
        response = requests.post(url, json=crypto.encryptData(sessionKey, data), headers=headers)
        return apiResponse.parseUser(response.json())
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return "User not found"

def keyExchange(username, public_key):
    url = endpoint + "keyExchange"
    data = {"username": username, "publicKey": public_key}
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json()
    except requests.exceptions.ConnectionError:
        return "Connection error"
    except requests.exceptions.HTTPError:
        if response.status_code == 500:
            return "Internal server error"