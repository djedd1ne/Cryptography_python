import cryptography

#Use symmetric encryption
from cryptography.fernet import Fernet

#Genetate a key
key = Fernet.generate_key()

#Create a Fernet object
cipher = Fernet(key)

#Store the key
with open("secret.key", "wb") as key_file:
  key_file.write(key)

#The message we want to encrypt
message = input("Message to encrypt: ").encode()
print("Original message: ", message.decode())

#Encrypt the message
encrypted_message = cipher.encrypt(message)
print("Secret message ", encrypted_message.decode())
