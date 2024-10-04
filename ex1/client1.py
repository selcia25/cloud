import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))
while True:
    message = input("Send message to server: ")
    try:
        if message.lower().strip() != 'exit':
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(f"Message received from server: {data}")
        else:
            break
    except ConnectionAbortedError as e:
        print(e)
client_socket.close()
    