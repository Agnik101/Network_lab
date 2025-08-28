
import socket

def udp_echo_client(server_ip='192.168.15.43', server_port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input("Enter message to send (or 'exit' to quit): ")
        if msg.lower() == 'exit':
            break

        sock.sendto(msg.encode(), (server_ip, server_port))

        data, _ = sock.recvfrom(1024)
        print("Received from server:", data.decode())

if __name__ == "__main__":
    udp_echo_client()
