## easy
## 32ms, 94.58%
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        ind=[]
        for i in range(len(s)):
            if s[i]==' ':
                ind.append(i)
        slen=len(s)
        for n in range(1,len(ind)+1): 
            if slen-ind[-n]-1==0:
                slen-=1
            elif slen-ind[-n]-1>0:
                return slen-ind[-n]-1
        return slen
            
        
