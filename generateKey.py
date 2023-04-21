from cryptography.fernet import Fernet

#generate symmetric key
key = Fernet.generate_key()

#save to file
with open("key.key", "wb") as file:
    file.write(key)
