import pickle
from socket import *
import Checksum as c
#import os

def notCurrupted(rcvpkt):
    data=rcvpkt[1]
    #print(data)
    checksum=rcvpkt[2]
    rcvDataCheck=c.CHECK(data)
    result=c.binaryAddition(rcvDataCheck,checksum)
    length=len(result)
    for i in range(0,length):
        if(result[i]!="1"):
            return False
            break
    return True
def hasSequenceNo(rcvpkt,actualSeq):
    if(rcvpkt[0]!=actualSeq):
        return False
    else:
        return True
def createPacket(Ack,seq,checkforAck):
    data1Tuple=(Ack,seq,checkforAck)
    return pickle.dumps(data1Tuple)
def udt_Send(packet,client):
    receiverSocket.sendto(packet,client)
def changeSeqNO(sequenceNum):
    if(sequenceNum==1):
        return 0
    else:
        return 1
    
receiverSocket=socket(AF_INET,SOCK_DGRAM)
receiverSocket.bind(("127.0.0.1",4500))
Ack=271
#Nak=282
seq=1
run=1
print('''Server is Started
This Server can't be stopped Normally.
To Stop It you should use Keyboard Exception''')

while(run):
    print("Server is waiting")
    seq=changeSeqNO(seq)
    #print("Data Received to the Sequence Number : "+str(seq))
    dataTuple,client=receiverSocket.recvfrom(2048)
    extractedTuple=pickle.loads(dataTuple)
    if(notCurrupted(extractedTuple) and hasSequenceNo(extractedTuple,seq)):
        print("With the Sequence Number "+str(seq)+" Received Data is "+str(extractedTuple[1]))
        packet1=createPacket(Ack,seq,c.compliment(c.CHECK(Ack)))
        udt_Send(packet1,client)
    elif(notCurrupted(extractedTuple)=="False"):
        if(seq==0):
            nseq=1
        else:
            nseq=0
        packet1=createPacket(Ack,nseq,c.CHECK(Nak))
        udt_Send(packet1,client)
    else:
        #Change in the sequence number
        packet1=createPacket(Ack,seq,c.compliment(c.CHECK(Ack)))
        udt_Send(packet1,client)