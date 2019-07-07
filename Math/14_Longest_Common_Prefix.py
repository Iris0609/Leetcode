
# easy
# 44ms, 41.25%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        long=strs[0]
        
        for i in range(1,len(strs)):
            if len(long)>len(strs[i]):
                long=strs[i]
                
        if not long:
            return ''
        for i in range(len(strs)):
            j=0
            while j<min(len(long),len(strs[i])):
                if long[j]==strs[i][j]:
                    j+=1
                    continue
                else:
                    long=long[:j]
                    
                    
                    
        return long
            
        