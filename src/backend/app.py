from flask import Flask, request, jsonify
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

@app.post('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == 'juan' and password == 'ed08c290d7e22f7bb324b15cbadce35b0b348564fd2d5f95752388d86d71bcca':  # juan PRUEBAS
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Login failed'})

@app.post('/newUser')
def newUser():
    rawData = request.get_json()
    data = ast.literal_eval(crypto.decryptData(sessionKey, rawData))
    username = data['username']
    password = data['password']

    #TODO: Save user in database
    return jsonify({'message': 'User created'})