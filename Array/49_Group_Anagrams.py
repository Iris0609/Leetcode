## 128ms
##58.99%
##medium

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            res.setdefault(''.join(sorted(s)),[]).append(s)
            
        return list(res.values())
                    
            
                