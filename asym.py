import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Generate public key
public_key = private_key.public_key()

# Encrypting the message with the public key
message = "I have a surprise for you".encode()

# Make secret message
encrypted_message = public_key.encrypt(
    message,
    cryptography.hazmat.primitives.asymmetric.padding.OAEP(
        mgf=cryptography.hazmat.primitives.asymmetric.padding.MGF1(algorithm=cryptography.hazmat.primitives.hashes.SHA256()),
        algorithm=cryptography.hazmat.primitives.hashes.SHA256(),
        label=None
    )
)

#Show secret message
print(encrypted_message)

#Decrypting the message with the private key
decrypted_message = private_key.decrypt(
    encrypted_message,
    cryptography.hazmat.primitives.asymmetric.padding.OAEP(
        mgf=cryptography.hazmat.primitives.asymmetric.padding.MGF1(algorithm=cryptography.hazmat.primitives.hashes.SHA256()),
        algorithm=cryptography.hazmat.primitives.hashes.SHA256(),
        label=None
    )
).decode()

print(decrypted_message)
