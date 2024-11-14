from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec, padding
from Crypto.Cipher import ChaCha20
from hashlib import sha256
from core import request
from env import dev

key = dev.chacha20Key

# Encrypts with the simmetric session key. BOTH.
def encryptText(sessionKey, message):
    nonce = sha256(sessionKey.encode()).digest()[:24]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(str(message).encode())
    return ciphertext.hex()

# Decrypts. BOTH.
def decryptText(sessionKey, ciphertext):
    nonce = sha256(sessionKey.encode()).digest()[:24]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    message = cipher.decrypt(bytes.fromhex(ciphertext))
    return message.decode()

# Generate client key pair. ECC SECP384R1. CLIENT SIDE.
def keyGen(userPassword):
    private_key = ec.generate_private_key(ec.SECP384R1())
    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(userPassword.encode())
    )
    public_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)

    with open("data/private_key.pem", "wb") as f:
        f.write(private_pem)
        
    return public_pem.hex()

# Send public key to server and retrieve session key. CLIENT SIDE.
def keyExchange(user, public_key):
    sessionKey = request.keyExchange(user, public_key)
    return sessionKey

# Encrypts the session key with the public key. SERVER SIDE.
def encryptKey(key, publicKey):
    public_key = serialization.load_pem_public_key(bytes.fromhex(publicKey))
    encrypted_text = public_key.encrypt(
        key.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_text.hex()

# Decrypts the session key with the private key. SERVER SIDE.
def decryptKey(encrypted_text):
    with open("data/private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    decrypted_text = private_key.decrypt(
        bytes.fromhex(encrypted_text),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_text.decode()


