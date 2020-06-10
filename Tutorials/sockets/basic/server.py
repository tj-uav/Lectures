import socket

IP, PORT = '127.0.0.1', 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, PORT))
sock.listen(1)
conn, addr = sock.accept()

receiving_data = conn.recv(1024).decode()
print("I received:", receiving_data)

sending_data = "Hello from server!"
print("I'm sending:", sending_data)
conn.send(sending_data.encode())

conn.close()
