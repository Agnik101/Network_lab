import socket
c=socket.socket()
port=9999

c.connect(('192.168.15.10', port))
print(c.recv(1024).decode())
c.close()
