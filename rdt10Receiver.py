from socket import *

receiverSocket=socket(AF_INET,SOCK_DGRAM)
receiverSocket.bind(("127.0.0.1",4500))

while(1):
    print("Server is waiting")
    message,client=receiverSocket.recvfrom(2048)
    print(message.decode())