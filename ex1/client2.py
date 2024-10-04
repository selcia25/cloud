import socket
import pickle

class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def __str__(self):
        return f"DataObject(name={self.name}, values={self.values})"
    
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))

name = input("Enter name: ")
values = eval(input("Enter list of values: "))
data_to_send = DataObject(name=name, values=values)
print(f"Sending object: {data_to_send}")

serialized_data = pickle.dumps(data_to_send)
client_socket.send(serialized_data)

response = client_socket.recv(1024).decode()
print(f"Received response from server: {response}")

client_socket.close()