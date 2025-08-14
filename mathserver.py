import socket
import threading
from datetime import datetime

LOG_FILE = "server_log.txt"

def calculate(expression):
    try:
        parts = expression.split()
        if len(parts) != 3:
            return "Error: Use format -> number operator number"
        num1, op, num2 = float(parts[0]), parts[1], float(parts[2])

        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2
        else:
            return "Error: Invalid operator"

        response = f"{num1} {op} {num2} = {result}"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as log:
            log.write(f"[{timestamp}] {response}\n")
        return response
    except:
        return "Error: Invalid input"

def handle_client(sock, addr):
    print(f"[+] Connected: {addr}")
    sock.send(b"Math Server Ready. Use: number operator number\n")
    while True:
        data = sock.recv(1024).decode().strip()
        if not data or data.lower() == 'exit':
            break
        result = calculate(data)
        sock.send(result.encode() + b"\n")
    print(f"[-] Disconnected: {addr}")
    sock.close()

def start_server(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Server running on {host}:{port}")
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()

if __name__ == "__main__":
    start_server()
