# Python 3.14.3
# STUDENT ID : 816041392

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

print('[Alice RSA key generation]')

# Generate private key
alice_private_key = rsa.generate_private_key(65537, 2048)
# Generate public key
alice_public_key = alice_private_key.public_key()

file_priv = 'aliceprivate.dat'
file_pub = 'alicepublic.dat'

# Write keys to .dat files
with open(file_priv, 'wb') as file:
    file.write(alice_private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    print(f'> Private key written to {file_priv}')

with open(file_pub, 'wb') as file:
    file.write(alice_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    print(f'> Public key written to {file_pub}')
