import bcrypt
import secrets
import uuid
import random
import json
from datetime import datetime
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def generated_employee_no():
    return datetime.now().strftime("%Y")

def encrypt(data):
    return fernet.encrypt(data.encode()).decode('utf-8')

def decrypt(data):
    data = bytes(data, 'utf-8')
    return fernet.decrypt(data).decode()

def stringify(data):
    return json.dumps(data)

def temp_password():
    return str(secrets.token_hex(3))

def hashedPassword(password):
    return  str(bcrypt.hashpw(password.encode(), bcrypt.gensalt()))

def checkPassword(password, storedPassword):
    storedPassword = storedPassword.replace(storedPassword[0:2],'')
    storedPassword = storedPassword.replace(storedPassword[len(storedPassword)-1:len(storedPassword)],'')
    if(bcrypt.checkpw(password.encode(), storedPassword.encode())):
        return True
    else:
        return False

def generated_token():
    return str(secrets.token_hex(10))


def generated_session_id():
    return str(uuid.uuid4())

