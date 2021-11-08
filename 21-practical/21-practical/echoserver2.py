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
    return data.decode('utf-8') 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1
s.bind(('127.0.0.1', 65432))                           # 2
s.listen()                                             # 3
while True:
    conn, addr = s.accept() 
    data = receive(conn)
    send(data, conn)
    data = recv(conn)
    conn.close() 


"""
Extend your echo server to use `send()` and `receive()` in 
the same way. You should be able to 
write those functions so that they can be
used in both the client and the server.
"""