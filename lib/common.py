"""
公共方法
"""

import hashlib


# SHA256加密密码
def sha256_encrypt(string: str):
    sha256 = hashlib.sha256()
    sha256.update(string.encode("utf-8"))
    encrypted_string = sha256.hexdigest()
    return encrypted_string


if __name__ == "__main__":
    pass
