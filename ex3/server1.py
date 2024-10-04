# Implement a Simple Message Passing System
# Create a message passing system where multiple processes communicate with each other using sockets. Each process will send and receive messages.

import socket
import threading

# To handle multiple clients
def handle_client(client_socket, addr):
    print(f"Connected to {addr}")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message or message.lower().strip() == 'exit':
                print(f"Client {addr} disconnected...")
                break
            response = input(f'Enter message to client {addr}: ')
            client_socket.send(response.encode())
        except Exception as e:
            print(f"Error: {e}")
    print(f"Connection closed with {addr}")
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen()
print("Server is listening...")

while True:
    client_socket, addr = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()