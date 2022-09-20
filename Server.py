import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

print("Waiting for connecttion")
connection, client_address = sock.accept()
print("A client connected")
#print("Client connected at: " + convertTuple(client_address))

while True:
    data = connection.recv(1024)
    print(data.decode("utf-8"))


