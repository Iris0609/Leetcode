## easy
## 84ms, 97.49%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=0
        s=str(x)
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                
            else:
                return False
            
        return True