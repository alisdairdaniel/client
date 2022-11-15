from socket import *

IP = '1.1.1.1'
SERVER_PORT = 40000
BUFLEN = 2048
dataSocket = socket(AF_INET, SOCK_STREAM)


dataSocket.connect((IP, SERVER_PORT))

while True:

    toSend = input('>>> ')
    if  toSend =='exit':
        break

    dataSocket.send(toSend.encode())


    recved = dataSocket.recv(BUFLEN)

    if not recved:
        break

    print(recved.decode())

dataSocket.close()
