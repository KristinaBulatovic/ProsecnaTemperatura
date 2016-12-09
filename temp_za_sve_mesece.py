from calendar import monthrange
import random
temp = [[-8,15],[-2,18],[0,22],[5,25],[10,30],[15,35],[15,45],[15,45],[10,30],[5,20],[0,15],[-5,12]]
meseci = ["januar", "februar", "mart", "april", "maj", "jun", "jul", "avgust", "septembar", "oktobar", "novembar", "decembar"]
b = 0
for i in meseci:
    f = open(i + ".txt", "w")
    dani = monthrange(2011, b+1)[1]
    for j in range(dani):
        f.write(str(random.randint(temp[b][0], temp[b][1]))+"\n")
    b+=1
f.close()


for i in meseci:
    f = open(i + ".txt", "r")
    s = 0
    b = 0
    for j in f:
        s+=int(j)
        b+=1
    prosecna = s/b
    print(i, "%.2f" % prosecna)
    
