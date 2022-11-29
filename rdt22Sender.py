from goto import *
from socket import *
import Checksum as c
import pickle

def make_pkt(Acknowledgement,data,checksum):
    datatuple=(Acknowledgement,data,checksum)
    return pickle.dumps(datatuple)

def udt_send(packet):
    senderSocket.sendto(packet,("127.0.0.1",4500))

def isACK(Acknowledgement,seq):
    if(Acknowledgement[0]!=271):
        return False
    else:
        if(seq==Acknowledgement[1]):
            return True
        else:
            return False
    

#def isNAK(Acknowledgement):
  #  if(Acknowledgement[0]==282):
    #    return True
    #else:
       # return False

def changeSeqNO(sequenceNum):
    if(sequenceNum==1):
        return 0
    else:
        return 1

def notCurrupted(rcvpkt,seq):
    data=rcvpkt[0]
    #print(data)
    checksum=rcvpkt[2]
    seqr=rcvpkt[1]
    rcvDataCheck=c.CHECK(data)
    result=c.binaryAddition(rcvDataCheck,checksum)
    length=len(result)
    for i in range(0,length):
        if(result[i]!="1"):
            #print("Acknowledgement is not currupted")
            return False
            break
    #print("Acknowledgement is not currupted")
    if(seqr==seq):
        return True
    else:
        return False

senderSocket=socket(AF_INET,SOCK_DGRAM)
seqNumdict={0:0,1:0}
senderSeq=1
Transmission=1
condition = 0
print('''Using this Sender Application You can send any value except "0" 
And Enter "0" to Stop this Application''')
while(Transmission):
    senderSeq=changeSeqNO(senderSeq)
    data=int(input("Enter the message for "+str(senderSeq)+" Sequence Number : " ))
    if(data==0):
        Transmission=0
        print("Sender Application has been Stopped")
        break
    seqNumdict[senderSeq]=data
    condition=1
    while(condition):
        packet=make_pkt(senderSeq,data,c.compliment(c.CHECK(data)))
        udt_send(packet)
        message,receiver= senderSocket.recvfrom(2048)
        #print(message)
        #print(receiver)
        extractedAck=pickle.loads(message)
        if(notCurrupted(extractedAck,senderSeq) and isACK(extractedAck,senderSeq)):
            print("Packet "+str(senderSeq)+" Sent Successfully and Acknowledged")
            condition=0
            break
        if((notCurrupted==False) or (isACK(extractedAck,senderSeq)==False)):
            print("Else condition become True")
            condition=1
            continue