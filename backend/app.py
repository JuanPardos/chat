from flask import Flask, request, jsonify

app = Flask(__name__)

@app.post('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == 'juan' and password == 'ed08c290d7e22f7bb324b15cbadce35b0b348564fd2d5f95752388d86d71bcca':  # juan PRUEBAS
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Login failed'})