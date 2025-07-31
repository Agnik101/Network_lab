import socket
HOST="127.0.0.1"
PORT=9999
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while (True):
        msg=input("enter message (or 'exit' to quit): ")
        if msg.lower()=='exit':
            break
        s.sendall(msg.encode())
        data=s.recv(1024)
        print("echoed:", data.decode())
