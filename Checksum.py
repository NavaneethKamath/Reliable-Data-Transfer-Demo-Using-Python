def decimalToBinary(n):  
    return bin(n).replace("0b", "")
def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal 
def length(binary,strglen):
    while(len(binary)!=strglen):
        binary="0"+binary
    return(binary)
def binaryAddition(n1,n2):
    sum=bin(int(n1,2)+int(n2,2))
    return sum.replace("0b", "")
def flip(c):
    if(c== '0'):
        return '1' 
    else:
        return '0'
def compliment(n):
    leng=len(n)
    onescomp=""
    for i in range(leng): 
        onescomp=onescomp+ flip(n[i])
    #ones = list(ones.strip("")) 
    return onescomp
   
def CHECK(decimal):
    #decimal=str(deci)
    binary=decimalToBinary(decimal)
    #print(binary)
    strglen=16*3
    strbinary=length(str(binary),strglen)
    #print(strbinary)
    sub1=strbinary[:16]
    sub2=strbinary[16:32]
    strbinary=strbinary[32:]
    sum1=binaryAddition(sub1,sub2)
    if(sum1==0):
        sum1="0000000000000000"
    sum2=binaryAddition(sum1,strbinary)
    if(len(sum2)>16):
        while(len(sum2)>16):
            sum2=str(sum2)
            sum2=sum2[1:]
            carry="0000000000000001"
            binaryAddition(str(sum2),carry)
    return sum2




