##medium
##dp
##952ms,70.21%

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxs=''
        def helper(s,l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            #for even case 'abba'
            tmp=helper(s,i,i+1)
            if len(tmp)>len(maxs):
                maxs=tmp
            #for odd case 'aba'
            tmp=helper(s,i,i)
            if len(tmp)>len(maxs):
                maxs=tmp
                
        return maxs