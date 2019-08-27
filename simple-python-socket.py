#simple socket python

import socket 
import sys 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serve_address = ('thborges.ddns.net', 80)

sock.connect(serve_address)

data = b"GET / HTTP/1.1\r\n"Insira URL"\r\n\r\n"

sock.sendall(data)

buf = []
lines = []
lastbyte = []

while 1: 
    byte = sock.recv(1)
    if byte == "\n":
        lines.append(buf)
        if lines [-1]  == ['\r','\n'] and buf == ['\r','\n']:
            break;
        buf = []
        
print(data)