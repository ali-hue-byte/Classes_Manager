import json
import os

from cryptography.fernet import Fernet
import hashlib
import re
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
import pickle

DATA_FILE = "data.pkl"
USER = "users.pkl"




def animate_title(title, start, end):
    if hasattr(title, "anim"):
        title.anim.stop()

    title.anim = QPropertyAnimation(title, b"pos")
    title.anim.setDuration(200)
    title.anim.setStartValue(start)
    title.anim.setEndValue(end)
    title.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
    title.anim.start()

def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            return pickle.load(f)
    else:
        return {}

def save(data):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)


def load_data():
    if os.path.exists(USER):
        with open(USER, "rb") as f:
            return pickle.load(f)
    else:
        return []

def save_data(data):
    with open(USER, "wb") as f:
        pickle.dump(data, f)




def KDF(password, salt):
    e_password = password.encode() if isinstance(password, str) else password
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    return Fernet(base64.urlsafe_b64encode(kdf.derive(e_password)))

def encrypt_data(data, password, KDF, salt):
    fernet = KDF(password, salt)
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data, password, KDF, salt):
    fernet = KDF(password, salt)
    return fernet.decrypt(data.encode()).decode()

def hash_password(password, salt):
    return hashlib.sha256(password.encode() + salt).hexdigest()


def check_strength(pss):

    tests = [len(pss) >= 8,
            bool(re.search(r"[A-Z]", pss)),
            bool(re.search(r"[a-z]", pss)),
            bool(re.search(r"[0-9]", pss)),
            bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pss))]
    return all(tests)




