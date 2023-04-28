import socket

host = '10.11.14.248'
port = 2034
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))


command = input('Command: ')
s.send(command.encode())
reply = s.recv(1024)
print(reply.decode('utf-8'))

s.close()
