import Pyro4

def call_remote_service():
    uri = input("Enter URI of the server (e.g., PYRO:obj_xxx@hostname:port): ")
    remote_calculator = Pyro4.Proxy(uri)
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    sum_result = remote_calculator.add_numbers(a, b)
    mul_result = remote_calculator.multiply(a, b)
    print(f"Sum of {a} and {b} (invoked remotely): {sum_result}")
    print(f"Multiplication of {a} and {b} (invoked remotely): {mul_result}")

if __name__ == "__main__":
    call_remote_service()