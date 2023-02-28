#CW1 test na http://data.pr4e.org/romeo-full.txt
import socket
url = input('Podaj url:')
HOST = url.split('/')
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((HOST[2], PORT))
except:
    print('invalid url')
    exit()
x = 'GET' + ' ' + url + ' ' + 'HTTP/1.0\r\n\r\n'
cmd = x.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()

#CW2 test na http://data.pr4e.org/romeo-full.txt
import socket
url = input('Podaj url:')
HOST = url.split('/')
PORT = 80
size = 0
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((HOST[2], PORT))
except:
    print('zły url')
    exit()
x = 'GET' + ' ' + url + ' ' + 'HTTP/1.0\r\n\r\n'
cmd = x.encode()
mysock.send(cmd)

y = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    y += data
y = y.decode()
print(y[:3000])
print('Długość pliku: ', len(y))

mysock.close()

#CW3 test na http://data.pr4e.org/romeo-full.txt
import urllib.request
url = input('Podaj url: ')
fhand = urllib.request.urlopen(url).read()
print(fhand[:3000].decode())
print('Długość pliku: ', len(fhand))

#CW4
import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Podaj url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
l = len(tags)
print('Liczba akapitów: ', l)

#CW5 http://data.pr4e.org/romeo-full.txt
url = input('Podaj url:')
HOST = url.split('/')
PORT = 80
size = 0
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((HOST[2], PORT))
except:
    print('invalid url')
    exit()
x = 'GET' + ' ' + url + ' ' + 'HTTP/1.0\r\n\r\n'
cmd = x.encode()
mysock.send(cmd)

y = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    y += data
pos = y.find(b"\r\n\r\n")
y = y[pos+4:].decode()
print(y)
mysock.close()
