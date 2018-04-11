from Crypto.Cipher import AES
import base64


ThePassword = raw_input("please input the password: ").rjust(64)
secret_key = '1234567890123456'

cipher = AES.new(secret_key,AES.MODE_ECB)
encoded = base64.b64encode(cipher.encrypt(ThePassword))
print encoded.strip()

