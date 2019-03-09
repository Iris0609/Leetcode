import sys
 
line=sys.stdin.readline().split(' ')
 
a=int(line[0])
b=int(line[1])
A=int(line[2])
B=int(line[3])
 
def cal_t(a,b,A,B):
    t=int(A/(2*a))
    resi=A-a*t*2
    p=int(resi/2)+resi%2
    if (B-b*2*t)==resi:
        return (t+p)
    else:
        return (-1)
     
print(cal_t(a,b,A,B))
