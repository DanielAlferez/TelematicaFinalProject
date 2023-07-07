from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import hmac

def generate_key(user_key):
    user_key = user_key.encode()
    key = user_key.ljust(32, b'\0')[:32]
    return key

def encrypt_message(message, key):
    key = generate_key(key)
    backend = default_backend()
    iv = b"0123456789abcdef" 
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend).encryptor()
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()
    encrypted_message = cipher.update(padded_message) + cipher.finalize()
    return encrypted_message

def decrypt_message(encrypted_message, key):
    try:
        key = generate_key(key)
        backend = default_backend()
        iv = b"0123456789abcdef"
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend).decryptor()
        padded_message = cipher.update(encrypted_message) + cipher.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_message = unpadder.update(padded_message) + unpadder.finalize()
        return decrypted_message.decode()
    except Exception as e:
        print("Error al descifrar")
        return None



# msg = input("ingrese mensaje: ")
# clave = input("ingrese clave: ")
# c = generate_key(clave)
# c_m = generate_key("saaaaa")
# msg_e = encrypt_message(msg,c)
# print(msg_e)

# msg_d = decrypt_message(msg_e,c)
# msg_m = decrypt_message(msg_e,c_m)
# print(msg_d)
# print(msg_m)
