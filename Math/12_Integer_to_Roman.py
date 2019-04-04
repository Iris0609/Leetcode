
## medium
## 92.82%,76ms
class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        l=[1000,500,100,50,10,5,1]
        res=''
        i=0
        while num!=0:
            if i<len(l)-1 and num-l[i+1]<0:
                i+=1
                continue
            if num//l[i]==0:
                if i<=len(l)-3 and num//(10**(len(str(l[i+2]))-1))==9:
                    res+=dic[l[i+2]]+dic[l[i]]
                    num-=9*l[i+2]
                    continue
                
                elif i<=len(l)-2 and num//(10**(len(str(l[i+1]))-1))==4:
                    res+=dic[l[i+1]]+dic[l[i]]
                    num-=4*l[i+1]
                    continue

                else:
                    i+=1
                    continue     
            
            else:
                res+=dic[l[i]]
                num-=l[i]
                
        return res
               
            
                
