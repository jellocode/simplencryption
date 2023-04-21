#read key and data from files
key = ""
with open("key.key", "rb")  as file:
    key = file.read()

edata = ""
with open("encryptedData.txt", "rb")  as file:
    edata = file.read()

from cryptography.fernet import Fernet
f = Fernet(key)

ddata = f.decrypt(edata)

print("Encrypted data: ", edata.decode())
print()
print("Decrypted data: ", ddata.decode())