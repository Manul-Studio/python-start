import socket

HOST = '127.0.0.1'
PORT = 8080
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind((HOST, PORT))
mysock.listen()
conn, addr = mysock.accept()
while True:
    print('Adres: ', addr)
    data = conn.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
    conn.sendall(b'PONG')

mysock.close()
