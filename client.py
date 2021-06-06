import socket

c=socket.socket()

c.connect(('localhost', 8000))

print(c.recv(1024).decode())