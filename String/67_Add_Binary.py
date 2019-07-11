
#easy
#40ms, beats 72.03%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ma=max(len(a),len(b))+1
        l=[0]*ma
        la=len(a)-1
        lb=len(b)-1
        ma=ma-1
        while la>=0 and lb>=0:
            tmp=int(a[la])+int(b[lb])+l[ma]
            l[ma]=tmp%2
            l[ma-1]+=tmp//2
            la-=1
            lb-=1
            ma-=1
        
        while la>=0:
            tmp=int(a[la])+l[ma]
            l[ma]=tmp%2
            l[ma-1]+=tmp//2
            la-=1
            ma-=1
        while lb>=0:
            tmp=int(b[lb])+l[ma]
            l[ma]=tmp%2
            l[ma-1]+=tmp//2
            lb-=1
            ma-=1
        start=0

        while start<len(l) and l[start]==0:
            start+=1
        if start==len(l):
            return '0'
        return ''.join(str(i) for i in l[start:])

        
        
        
        
                
                
        