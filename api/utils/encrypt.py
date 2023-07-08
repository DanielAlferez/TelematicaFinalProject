from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib
import hmac

def generate_key(clave_personalizada):
    clave_personalizada = clave_personalizada.encode()
    clave = clave_personalizada.ljust(32, b'\0')[:32]
    return clave

def encrypt_message(mensaje, clave):
    backend = default_backend()
    iv = b"0123456789abcdef" 
    cifrador = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=backend).encryptor()
    padder = padding.PKCS7(128).padder()
    mensaje_pad = padder.update(mensaje.encode()) + padder.finalize()
    mensaje_cifrado = cifrador.update(mensaje_pad) + cifrador.finalize()
    mensaje_cifrado_hex = mensaje_cifrado.hex()  # Convertir a representación hexadecimal
    return mensaje_cifrado_hex

def decrypt_message(mensaje_cifrado_hex, clave):
    try:
        backend = default_backend()
        iv = b"0123456789abcdef"
        descifrador = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=backend).decryptor()
        mensaje_cifrado = bytes.fromhex(mensaje_cifrado_hex)  # Convertir de representación hexadecimal a bytes
        mensaje_pad = descifrador.update(mensaje_cifrado) + descifrador.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        mensaje_descifrado = unpadder.update(mensaje_pad) + unpadder.finalize()
        return mensaje_descifrado.decode()
    except Exception as e:
        print("Error al desencriptar")
        return None



