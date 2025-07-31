import socket
s=socket.socket()
print("socket created successfully")
port=9999
s.bind(("",port))
print("socket binded to %s " %(port))
s.listen(5)
print("socket is listening")
while(True):
    
    c,addr = s.accept()
    print("got connection from",addr)
    c.send(bytes('hey thanks for joining!','utf=8'))
    
