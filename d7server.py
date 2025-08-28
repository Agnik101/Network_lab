import socket

def udp_echo_server(host='', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    total_messages = 0

    while True:
        data, addr = sock.recvfrom(1024)
        total_messages += 1

        
        message = data.decode().upper()

        
        response = f"{message} | Total messages: {total_messages}"
        sock.sendto(response.encode(), addr)

if __name__ == "__main__":
    udp_echo_server()
