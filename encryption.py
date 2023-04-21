#read key and data from files
key = ""
with open("key.key", "rb")  as file:
    key = file.read()

data = ""
with open("data.txt", "rb")  as file:
    data = file.read()

#encrypt data, save
from cryptography.fernet import Fernet
f = Fernet(key)

edata = f.encrypt(data)

with open("encryptedData.txt", "wb") as file:
    file.write(edata)