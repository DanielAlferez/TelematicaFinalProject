from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_message(message, key):
    key = key.encode()
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    key = key.encode()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    unpadded_message = unpad(decrypted_message, AES.block_size)
    return unpadded_message.decode()
