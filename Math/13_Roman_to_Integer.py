# easy
# 95.82%, 68ms
class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        i=0
        res=0
        while i<len(s):
            if (s[i]=='I' or s[i]=='X' or s[i]=='C') and i<len(s)-1:
                if dic[s[i+1]]>dic[s[i]]:
                    res+=dic[s[i+1]]-dic[s[i]]
                    i+=2
                    continue
                else:
                    res+=dic[s[i]]
                    i+=1
                    continue
                    
            else:
                res+=dic[s[i]]
                i+=1
                continue
        return res
                    
            
                    
            
            
            