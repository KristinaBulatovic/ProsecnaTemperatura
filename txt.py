import random

def txtFile():
    temp = [[-5,10],[-5,10],[10,18],[10,28],[10,28],[19,40],[29,40],[29,40],[29,40],[4,16],[4,16],[-3,9]]
    meseci = ["januar","februar","mart","april","maj","jun","jul","avgust","septembar","oktobar","novembar","decembar"]
    f = None
    for i in range(len(meseci)):
        f = open(meseci[i]+".txt","w")
        if meseci[i] == "april" or meseci[i] == "jun" or meseci[i] == "septembar" or meseci[i] == "novembar":
            for j in range(30):
                f.write(str(random.randrange(temp[i][0],temp[i][1]+1)) + "\n")
            f.close()
        elif meseci[i] == "februar":
            for j in range(28):
                f.write(str(random.randrange(temp[i][0],temp[i][1]+1)) + "\n")
            f.close()
        else:
            for j in range(31):
                f.write(str(random.randrange(temp[i][0],temp[i][1]+1)) + "\n")
            f.close()

txtFile()
