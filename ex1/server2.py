# Modify the client-server application to send and receive user-defined objects

import socket
import pickle

class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values
    def __str__(self):
        return f"DataObject(name={self.name}, values={self.values})"
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen()
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    try:
        received_data = client_socket.recv(1024)

        if not received_data:
            print("No data received. Closing connection.")
            break
        data_object = pickle.loads(received_data)
        print(f"Received object from client: {data_object}")
        total_sum = sum(data_object.values)
        response = f"Server: Received {data_object.name}'s data. Sum = {total_sum}"
        client_socket.send(response.encode())
    except Exception as e:
        print(f"Error: {e}")
        break
client_socket.close()
server_socket.close()