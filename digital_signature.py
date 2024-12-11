import hashlib

def make_signature(message):
    return hashlib.sha256(message.encode()).hexdigest()

document = "Hello World"
signature = make_signature()

print(document)
print(signature)
