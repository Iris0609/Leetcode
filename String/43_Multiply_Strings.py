
#medium
#156ms, beats 41.28%
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l=len(num1)+len(num2)
        res=[0]*l
        pos=len(res)-1
        
        for n1 in reversed(num1):
            tmpos=pos
            for n2 in reversed(num2):
                tmp=int(n1)*int(n2)
                res[tmpos-1]+=(res[tmpos]+tmp)//10
                res[tmpos]=(res[tmpos]+tmp)%10
                tmpos-=1
            pos-=1
        s=''  
        start=0
        ##take care if the result equals to 0
        while res[start]==0 and start!=len(res)-1:
            start+=1
            
        for n in res[start:]:
            s+=str(n)
            
        return s