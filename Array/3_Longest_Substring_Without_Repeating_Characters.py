##array
##76ms,90.17%
##medium
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        start=0
        dic={}
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]]>=start:
                start=dic[s[i]]+1
            else:
                maxl=max(maxl,i-start+1)
            dic[s[i]]=i
            
        return maxl
                