import socket

IP, PORT = '127.0.0.1', 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

sending_data = "Hello from client!"
print("I'm sending:", sending_data)
sock.send(sending_data.encode())

receiving_data = sock.recv(1024).decode()
print("I received:", receiving_data)

sock.close()
