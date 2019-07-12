
#medium
#40ms, 63.81%

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp=[0 for _ in range(len(s)+1)]
        dp[0]=1
        for i in range(1,len(s)+1):
            if s[i-1]!="0":
                dp[i]+=dp[i-1]
            if i>1 and s[i-2:i]>"09" and s[i-2:i]<"27":
                dp[i]+=dp[i-2]
                
        return dp[-1]
                
      