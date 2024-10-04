# Develop an RMI-based distributed application where the server provides a remote service, and the client invokes this service.

# pip install pyro4
import Pyro4

# Remote service class
@Pyro4.expose
class Calculator:
    def add_numbers(self, a, b):
        return a+b
    def multiply(self, a, b):
        return a*b
    
# Start Pyro4 Daemon to expose remote service
def start_server():
    daemon = Pyro4.Daemon()
    uri = daemon.register(Calculator)
    print(f"Server is ready. URI: {uri}")
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()