from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from Crypto.Cipher import ChaCha20
from backend.env import dev
from core import request

seed = dev.simmetricSeed

# Encrypts with the simmetric session key.
def encryptData(sessionKey, message):
    cipher = ChaCha20.new(key=seed, nonce=bytes.fromhex(sessionKey))
    ciphertext = cipher.encrypt(str(message).encode())
    return ciphertext.hex()

def decryptData(sessionKey, ciphertext):
    hex_ciphertext = ciphertext.text.strip().strip('"') 
    cipher = ChaCha20.new(key=seed, nonce=bytes.fromhex(sessionKey))
    message = cipher.decrypt(bytes.fromhex(hex_ciphertext))
    return message.decode()

# Generate client key pair. RSA 2048 bits. CLIENT SIDE.
def keyGen(userPassword):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(userPassword.encode())
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("data/private_key.pem", "wb") as file:
        file.write(private_pem)
        
    return public_pem.hex()

# Send public key to server and retrieve session key. CLIENT SIDE.
def keyExchange(user, public_key):
    sessionKey = request.keyExchange(user, public_key)
    return sessionKey

# Decrypts the session key with the private key. CLIENT SIDE.
def decryptKey(encryptedKey, userPassword):
    with open("data/private_key.pem", "rb") as key_file:
        privateKey = serialization.load_pem_private_key(
            key_file.read(), 
            password=userPassword.encode()
        )

    decryptedKey = privateKey.decrypt(
        bytes.fromhex(encryptedKey),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decryptedKey.hex()
