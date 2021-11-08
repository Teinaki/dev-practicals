import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 65432))
x = input('Enter a message: ')
x_str_as_bytes = x.encode()
s.sendall(x_str_as_bytes)
data = s.recv(1024)  
print(data)                                  
s.close()         


"""
1. **Echo client**: The client isn't much different from the example client code we just saw. Write a client that
    1. connects to a server on the localhost;
    2. gets a message from user input;
    3. sends the message to the server;
    4. receives the echoed response from the server;
    5. prints the response;
    6. closes the connection.
    """