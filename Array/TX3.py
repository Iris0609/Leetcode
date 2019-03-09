import sys
 
def cal_dis(x1,x2,y1,y2):
    return (x1-x2)**2+(y1-y2)**2
 
def square(x,y):
    dic=[]
    ox=int(x[0])
    oy=int(y[0])
    for j in range(1,4):
        cnt=0
        dic.append(cal_dis(ox,int(x[j]),oy,int(y[j])))
        if max(dic)==min(dic):
            continue
        if max(dic)!=min(dic) and 2*min(dic)**2==max(dic)**2:
            cnt+=1
            for i in range(1,4):
                if i==j:
                    continue
                elif min(dic)!=cal_dis(int(x[j]),int(x[i]),int(y[j]),int(y[i])):
                    return('No')
 
    if len(set(dic))!=2 or cnt!=1:
        return ("No")
    return("Yes")
         
 
n=int(sys.stdin.readline())
 
for i in range(n):
    x=sys.stdin.readline()
    y=sys.stdin.readline()
     
    print(square(x,y))