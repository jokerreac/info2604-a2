# STUDENT ID : 816041392

import socket
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

host = socket.gethostname()
port_message = 5001

# Create socket for Alice's message server
socket_message = socket.socket()

try:
    socket_message.bind((host, port_message))
    socket_message.listen()

    print(f'[Alice] Waiting to send message on port#{port_message} ...')

    conn, addr = socket_message.accept()

    try:
        # Load Alice's private key
        with open("aliceprivate.dat", "rb") as file:
            alice_private_key = serialization.load_pem_private_key(
                file.read(),
                password=None
            )
        print('> Private key loaded')

        # Message
        message = 'The rapid deployment of AI is outpacing regulation, leading to risks regarding data privacy, algorithmic bias, and misinformation'
        message_bytes = message.encode('utf-8')

        # Sign message using Alice's private key
        signature = alice_private_key.sign(
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print('> Message signed using private key')

        # Send message and signature to Bob
        conn.sendall(message_bytes)
        print('> Message sent successfully')
        conn.sendall(signature)
        print('> Signature sent successfully')

    except FileNotFoundError:
        print('> Error: aliceprivate.dat not found')

    except Exception as e:
        print(f'> Connection error: {e}')

except Exception as e:
    print(f'> Server error: {e}')

finally:
    conn.close()
    print('> Connection closed')
    socket_message.close()
    print('> sendmessage.py terminated')