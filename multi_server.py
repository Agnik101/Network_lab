import socket
import threading,time

def handle_client(conn):
    while data := conn.recv(1024):
        if not data: break
        print("received:", data.decode(),"at time:",time.ctime())
        conn.sendall(data)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0',9999))
    s.listen()
    print("socket is listening")
    while True:
        conn, _ = s.accept()
        threading.Thread(target=handle_client, args=(conn,), daemon=True).start()
