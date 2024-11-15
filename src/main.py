from core import request
from utils import crypto

# Start
# TODO: Ask for server endpoint if desired
input_loginOrSignUp = input("Do you want to [L]ogin or [S]ign up?: ")

if input_loginOrSignUp == "S":
    input_userName = input("Enter your username: ")
    input_password = input("Enter your password: ")
    key = crypto.keyGen(input_password)
    sessionKey = crypto.decryptKey(crypto.keyExchange(input_userName, key), input_password)
    
    user = request.newUser(sessionKey, input_userName, input_password)
elif input_loginOrSignUp == "L":
    input_userName = input("Enter your username: ")
    input_password = input("Enter your password: ")
else:
    print("Invalid option")
    exit()



""" publicKey = crypto.keyGen("password")
key = crypto.keyExchange("juan", publicKey)
#print(key)
print(crypto.decryptKey(key, "password"))
 """