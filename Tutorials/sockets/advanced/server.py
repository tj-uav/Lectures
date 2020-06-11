import socket
from threading import Thread


def continuously_recv(connection):
    while True:
        data = connection.recv(1024)
        print("Received:", data)


IP, PORT = '127.0.0.1', 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen(1)
conn, addr = sock.accept()

recv_thread = Thread(target=continuously_recv, args=(conn,))
recv_thread.daemon = True
recv_thread.start()

while True:
    inp = input("What would you like to send to client?\n")
    conn.send(inp.encode())

conn.close()
sock.close()
