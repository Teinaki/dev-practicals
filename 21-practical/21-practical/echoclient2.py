import socket
import struct

def send(txt, sock):
  msgbody = bytes(txt.encode('utf-8'))
  msglen = len(msgbody)
  header = struct.pack('>H', msglen) # 2-byte unsigned int
  message = header + msgbody
  sock.sendall(message) 

def receive(sock):
    data = b''
    while len(data) < 2:
        data += sock.recv(4)
    body_length  = struct.unpack('>H', data[:2])[0]
    data = data[2:]
    while len(data) < body_length:
        data += sock.recv(4)
    return data[:body_length].decode('utf-8') 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 65432))
x = input('Enter a message: ')
send(x, s)
data = receive(s)
print(data)                                  
s.close() 

"""Extend your echo client to use `send()` and `receive()` 
functions that add and process our basic 
two-byte length header, repectively."""