import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "192.168.0.36"
#host = socket.gethostname()

port = 8080

# connection to hostname on the port.
s.connect((host, port))
s.send("Bhosadike".encode())

# Receive no more than 1024 bytes
msg = s.recv(1024)

s.close()
print (msg.decode('ascii'))