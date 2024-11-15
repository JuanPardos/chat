from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from Crypto.Cipher import ChaCha20
from datetime import datetime
from hashlib import sha256
from env import dev

seed = dev.simmetricSeed

def genSessionKey(userName):
    date = str(datetime.now())
    key = sha256((userName + date).encode()).digest()[:12]
    return key

# Encrypts data with the session key
def encryptData(key, data):
    cipher = ChaCha20.new(key=seed, nonce=key)
    ciphertext = cipher.encrypt(str(data).encode())
    return ciphertext.hex()

# Decrypts data with the session key
def decryptData(key, ciphertext):
    cipher = ChaCha20.new(key=seed, nonce=key)
    message = cipher.decrypt(bytes.fromhex(ciphertext))
    return message.decode()

# Encrypts the session key with the public key
def encryptKey(key, publicKey):
    public_key = serialization.load_pem_public_key(bytes.fromhex(publicKey))
    encryptedKey = public_key.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encryptedKey.hex()