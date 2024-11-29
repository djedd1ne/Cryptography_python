# Import cryptogaphy library
import cryptography

# Use a symmetric encryption method
from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file: # with, no need to close the file
    key = key_file.read()

# Create a Fernet object
cipher = Fernet(key)

# Input secret message
encrypted_message = input("Secret message: ").encode()

# Decrypt the message
message = cipher.decrypt(encrypted_message)

# Print the original message
print("Original message: ", message.decode())
