# STUDENT ID : 816041392

import socket
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

host = socket.gethostname()
port_public_key = 5000
port_message = 5001

# Create sockets for receiving public key and message
socket_public_key = socket.socket()
socket_message = socket.socket()

try:
    # Request Alice's public key
    socket_public_key.connect((host, port_public_key))
    socket_public_key.sendall('REQUEST_PUBLIC_KEY'.encode('utf-8'))
    print('> Requested public key')

    alice_public_key = socket_public_key.recv(1024)
    alice_public_key = serialization.load_pem_public_key(alice_public_key)
    print('> Public key received and loaded')

    # Receive message and signature from Alice
    socket_message.connect((host, port_message))

    alice_message = socket_message.recv(1024)
    print('> Message received')

    alice_signature = socket_message.recv(1024)
    print('> Signature received')

    # Verify signature for authentication and integrity
    try:
        alice_public_key.verify(
            alice_signature,
            alice_message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print('> Authentication and integrity checks were successful')

    except InvalidSignature:
        print('> Authentication/integrity check failed: invalid signature')

except Exception as e:
    print(f'> Connection error: {e}')

finally:
    socket_public_key.close()
    socket_message.close()
    print('> Connections closed')
    print('> bobsprogram.py terminated')