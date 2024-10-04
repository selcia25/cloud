# Create a simple client-server application where the server provides a service and the client communicates with it.

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen()
client_socket, addr = server_socket.accept()
print(f"Connected {client_socket} on {addr}")

while True:
    message = client_socket.recv(1024).decode()
    try:
        # Check if the message is empty (client may have closed the connection)
        if not message:
            print("No message received. Client may have closed the connection.")
            break

        # Check if the message is 'exit'
        if message.lower().strip() == 'exit':
            print("Received 'exit' message. Closing connection.")
            break

        
        print(f"Message received from client: {message}")
        list1 = message.split()
        total_sum = 0
        for i in list1:
            total_sum += int(i)
        # data = input(f"Send to client: ")
        response = client_socket.send(str(total_sum).encode())
        print(f"Sending data {total_sum} to client")
        
        
    except ConnectionAbortedError as e:
        print(e)
client_socket.close()
server_socket.close()