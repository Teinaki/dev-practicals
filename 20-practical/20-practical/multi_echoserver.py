import socket
import selectors

host = '127.0.0.1' 
port = 65432

def accept_connection(sock, clients):
    conn, addr = sock.accept()
    conn.setblocking(False)
    data = {'addr': addr, 'buffer': b''}
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    clients.register(conn, events, data=data)

def service_connection(event, mask, clients):
    sock = event.fileobj
    data = event.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data['buffer'] = recv_data
        else:
            clients.unregister(sock)
            sock.close()
        if mask & selectors.EVENT_WRITE:
            if data['buffer']:
                sock.sendall(data['buffer'])
                data['buffer'] = b''

clients = selectors.DefaultSelector()
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind((host, port))
listener.listen()
listener.setblocking(False)
clients.register(listener, selectors.EVENT_READ, data=None)
while True:
    events = clients.select(timeout=None)
    for event, mask in events:
        if event.data is None:
            accept_connection(event.fileobj, clients)
        else:
            service_connection(event, mask, clients)