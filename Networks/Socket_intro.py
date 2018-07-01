import socket
myscok=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myscok.connect(('data.pr4e.org', 80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
myscok.send(cmd)

while True:
    data=myscok.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
myscok.close()
