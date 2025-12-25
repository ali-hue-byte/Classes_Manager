import json
import os

from cryptography import fernet
from cryptography.fernet import Fernet
import hashlib
import re
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64





USER = "users.json"
SALT_file = "salt"
def load_data():
    if os.path.exists(USER):
        with open(USER, "r") as f:
            return json.load(f)
    else:
        return []

def save_data(data):
    with open(USER, "w") as f:
        return json.dump(data, f, indent=4)


def SALT():
    if os.path.exists(SALT_file):
        with open(SALT_file, "r") as f:
            salt = bytes.fromhex(f.read())
    else:
        salt = os.urandom(16)
        with open(SALT_file, "w") as f:
            f.write(salt.hex())
    return salt

def KDF(password, salt):
    e_password = password.encode() if isinstance(password, str) else password
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return Fernet(base64.urlsafe_b64encode(kdf.derive(e_password)))

def encrypt_data(data, password, KDF, salt):
    fernet = KDF(password, salt)
    return fernet.encrypt(data.encode()).decode()

def hash_password(password, salt):
    return hashlib.sha256(password.encode() + salt).hexdigest()


def check_strength(pss):

    tests = [len(pss) >= 8,
            bool(re.search(r"[A-Z]", pss)),
            bool(re.search(r"[a-z]", pss)),
            bool(re.search(r"[0-9]", pss)),
            bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pss))]
    return all(tests)


