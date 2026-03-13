from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

alice_private_key = rsa.generate_private_key(65537, 2048)
alice_public_key = alice_private_key.public_key()

with open('aliceprivate.dat', 'wb') as file:
    file.write(alice_private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))

with open('alicepublic.dat', 'wb') as file:
    file.write(alice_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))

