import socket
import sys

HOST_IP, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    sock.connect((HOST_IP, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    received = str(sock.recv(1024), "utf-8")

print("Sent: {}".format(data))
print("Recv: {}".format(received))