# crypto/utils.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
import base64
from django.shortcuts import render
from django.http import HttpResponse


def encrypt_image(image_path, key):
    with open(image_path, 'rb') as f:
         image_data = f.read()#plaintext = f.read()

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(image_data, AES.block_size))

    return base64.b64encode(cipher.iv + ciphertext).decode('utf-8')

def decrypt_image(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext