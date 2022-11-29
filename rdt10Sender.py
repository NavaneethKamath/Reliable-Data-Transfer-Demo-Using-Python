from socket import *
def make_pkt(data):
    return data.encode()
def udt_send(packet):
    senderSocket.sendto(packet,("127.0.0.1",4500))

Transmission=1
senderSocket=socket(AF_INET,SOCK_DGRAM)
print('''Using this Sender Application You can send any value except "0" 
And Enter "0" to Stop this Application''')
while(Transmission):
    data=(input("Enter the message : "))
    if(data=="0"):
        Transmission=0
        print("Sender Application has been Stopped")
        break
    packet=make_pkt(data)
    udt_send(packet)
    

    

                    
