import socket

def start_client(host='localhost', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        print(client.recv(1024).decode())  

        while True:
            expr = input("Enter expression (or 'exit' to quit): ")
            client.send(expr.encode())
            if expr.lower() == 'exit':
                break
            response = client.recv(1024).decode()
            print("Server:", response)

if __name__ == "__main__":
    start_client()
