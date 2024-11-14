from classes.User import User
from utils import crypto

public_key = crypto.keyGen("TEST")
text = crypto.encryptKey("TEST", public_key)

#x = crypto.encrypt("user", "message")
#print(crypto.decrypt("user", x))
