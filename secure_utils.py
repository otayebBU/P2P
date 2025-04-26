
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b"1234567890abcdef"  # 16-byte AES key

def encrypt(msg):
    cipher = AES.new(KEY, AES.MODE_CBC)  # Using CBC for better security
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(msg.encode(), AES.block_size))
    return iv + ciphertext

def decrypt(ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size).decode()

