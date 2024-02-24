from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

from padding import pad, unpad

key = os.urandom(32)
iv = os.urandom(16) # AESブロックサイズ

data = b"Hello, World! This is a secret message."

# 暗号化器の設定
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

# 復号化器の設定
decryptor = cipher.decryptor()

def main():
    padded_data = pad(data)
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    decrypted_data = unpad(decrypted_padded_data)

    original_data = decrypted_data.decode('utf-8')

    print(original_data)


if __name__ == "__main__":
    main()
