import sys


line1=sys.stdin.readline().split(" ")
line2=sys.stdin.readline().split(" ")
line3=sys.stdin.readline().split(" ")

n=int(line1[0])
m=int(line1[1])

magiclist=[]

k=1
for i in range(len(line2)):
    magiclist.append(int(line2[i]))
    while (i+1)==int(line3[k-1]):
        magiclist.sort()
        print(magiclist[k-1])
        k+=1

        

    
    
    

