import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1
s.bind(('127.0.0.1', 65432))                           # 2
s.listen()                                             # 3
while True:
    conn, addr = s.accept() 
    data = conn.recv(1024)
    conn.sendall(data)
    data = conn.recv(1024)
    conn.close() 


"""
2. **Echo server**: The echo server needs just a bit more capability than the example code. Write a server that
    1. sets up a socket listening on the localhost interface (IPv4);
    2. accepts the incoming client connection;
    3. in a loop, receives data from the client and sends the same data back;
    4. exits the loop when it receives empty data (this indicates that the client closed the connection);
    5. closes its connection.
"""