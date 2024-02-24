from cryptography.hazmat.primitives import padding

# パディング関数
def pad(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return padded_data

# パディング削除関数
def unpad(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data)
    data += unpadder.finalize()
    return data
