import json
import os


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

def hash_password(password, salt):
    return hashlib.sha256(password.encode() + salt).hexdigest()


def check_strength(pss):

    tests = [len(pss) >= 8,
            bool(re.search(r"[A-Z]", pss)),
            bool(re.search(r"[a-z]", pss)),
            bool(re.search(r"[0-9]", pss)),
            bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pss))]
    return all(tests)

def check_user(username):
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", username):
        return True

