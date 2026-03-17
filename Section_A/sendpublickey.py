# Python 3.14.3
# STUDENT ID : 816041392

import socket

host = socket.gethostname()
port_public_key = 5000

# Create socket for Alice's public key server
socket_public_key = socket.socket()

try:
    socket_public_key.bind((host, port_public_key))
    socket_public_key.listen()

    print(f'[Alice] Waiting for public key request on port#{port_public_key} ...')

    conn, addr = socket_public_key.accept()

    try:
        # Receive request command from Bob
        request = conn.recv(1024).decode('utf-8')

        if request == 'REQUEST_PUBLIC_KEY':
            print('> Request received')

            # Read and send Alice's public key
            with open('alicepublic.dat', 'rb') as file:
                alice_public_key = file.read()

            conn.sendall(alice_public_key)
            print('> Public key sent successfully')

        else:
            print('> Invalid request received')

    except FileNotFoundError:
        print('> Error: alicepublic.dat not found')

    except Exception as e:
        print(f'> Connection error: {e}')

except Exception as e:
    print(f'> Server error: {e}')

finally:
    conn.close()
    print('> Connection closed')
    socket_public_key.close()
    print('> sendpublickey.py terminated')