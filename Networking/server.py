import socket

s = socket.socket()
print('Socket is created.')

s.bind(('', 99))

s.listen(3)

print('Waiting for connections..')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()

    print('Connected with ', addr, name)

    c.send(bytes('The connection was Successfull. This is your message.', 'utf-8'))

    c.close()