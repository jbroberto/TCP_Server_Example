import socket
import re

HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def matches(pwd):
    return re.match("[a-zA-Z+],[0-9+]", pwd) is not None

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    data = raw_input("type a message: ")
    if matches(data):
        sock.sendall(data + "\n")
    else:
        print "You typed an invalid sequence. Try again\n"
        data = raw_input("type a message: ")

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)