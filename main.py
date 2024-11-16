from core import request
from utils import crypto
import getpass

# Start
# TODO: Ask for server endpoint if desired
input_loginOrSignUp = input("Do you want to [L]ogin or [S]ign up?: ")
input_userName = input("Enter your username: ")
input_password = getpass.getpass("Enter your password: ")
key = crypto.keyGen(input_password)
sessionKey = crypto.decryptKey(crypto.keyExchange(input_userName, key), input_password)

if input_loginOrSignUp == "S":
    user = request.newUser(sessionKey, input_userName, input_password)
    if user != None:
        print("Welcome " + user.username)
    else:
        print("User registration failed")
    exit()
elif input_loginOrSignUp == "L":
    user = request.login(sessionKey, input_userName, input_password)
    if user != None:
        print("Welcome " + user.username)
    else:
        print("Invalid credentials")
else:
    print("Invalid option")
    exit()



""" publicKey = crypto.keyGen("password")
key = crypto.keyExchange("juan", publicKey)
#print(key)
print(crypto.decryptKey(key, "password"))
 """