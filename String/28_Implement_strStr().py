#easy
#40ms, 51.86%

 Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen=len(haystack)
        nlen=len(needle)
        i=0
        j=0
        
        while(i<hlen) and (j<nlen):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            
            else:
                i=i-j+1
                j=0
                
        
        if j==nlen:
            return i-j
        else:
            return -1

        #### method 2
        # for i in range(hlen-nlen+1):
        #     if haystack[i:i+nlen]==needle:
        #         return i

        # return -1