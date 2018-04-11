from Crypto.Cipher import AES
import base64

file = open('try_to_decrypt_me','r').read()

secret_key = '1234567890123456'

cipher = AES.new(secret_key,AES.MODE_ECB)
decoded = cipher.decrypt(base64.b64decode(file))

print decoded.strip()

