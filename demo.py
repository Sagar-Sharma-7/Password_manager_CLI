import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.fernet import Fernet


def fetch_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password?: ") # master_pwd = sagar
key = fetch_key()# encode - takes your string and turns it into bytes
fer = Fernet(key)

# one time running function to generate a key for master_pwd
'''
def make_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

make_key();
'''


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")

# menu
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit: ")
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    elif mode.lower() == "q":
        break
    else: 
        print("Invalid mode.")
        continue