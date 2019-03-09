import sys
import math
 
n=int(sys.stdin.readline())
dic={-1:0,0:1}
 
def getmoney(n):
    if n in dic:
        return dic[n]
    else:
        m=int(math.log2(n))
        method=getmoney(n-2**m)+getmoney(2**(m+1)-n-2)
        dic[n]=method
        return method
print(getmoney(n))