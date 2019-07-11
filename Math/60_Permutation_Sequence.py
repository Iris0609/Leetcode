
#medium
#36ms, beats 77.18%
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        def nth(li,k,res):
            if k==math.factorial(len(li)):
                res+=li[::-1]
                return res
            if len(li)==1 or k==1:
                res+=li
                return res
            
            tmpl=len(li)-1
            ind=math.ceil(k/math.factorial(tmpl))-1
            res+=li[ind]
            k-=ind*math.factorial(tmpl)
            return nth(li[:ind]+li[ind+1:],k,res)
        
            
        s=''.join(str(i) for i in range(1,n+1))
        res=nth(s,k,'')
        return res