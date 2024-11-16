from flask import Flask, request, jsonify
from services import userService
from hashlib import sha256
import crypto
import ast

app = Flask(__name__)

sessionKey = None

@app.post('/keyExchange')
def keyExchange():
    global sessionKey

    data = request.get_json()
    user = data.get('username')
    publicKey = data.get('publicKey')
    sessionKey = crypto.genSessionKey(user)
    encryptedKey = crypto.encryptKey(sessionKey, publicKey)
    return jsonify(encryptedKey)

@app.post('/newUser')
def newUser():
    rawData = request.get_json()
    data = ast.literal_eval(crypto.decryptData(sessionKey, rawData))
    username = data['username']
    password = sha256(data['password'].encode()).hexdigest()
    
    user = userService.insert(username, password)
    return jsonify(crypto.encryptData(sessionKey,user))

@app.post('/login')
def login():
    rawData = request.get_json()
    data = ast.literal_eval(crypto.decryptData(sessionKey, rawData))
    username = data['username']
    password = sha256(data['password'].encode()).hexdigest()
    
    user = userService.get(username, password)
    return jsonify(crypto.encryptData(sessionKey,user))