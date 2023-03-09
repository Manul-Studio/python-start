import socket

HOST = '127.0.0.1'
PORT = 8080
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'ping')


mysock.close()
