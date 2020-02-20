import socket

s = socket.socket()
host = 'localhost'
port = 13854

mess = '{"enableRawOutput" : true, "format" : "Json"}'.encode()

s.connect((host, port))
s.sendall(mess)
data = s.recv(2048)

while data is not None:
    print(repr(data))