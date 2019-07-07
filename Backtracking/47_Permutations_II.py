#medium
# 68ms, 96.5%
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        def backtracking(tmp,n):
            if not n:
                res.append(tmp)
                return
            for i in range(len(n)):
                if i>0 and n[i]==n[i-1]:
                    continue
                backtracking(tmp+[n[i]],n[:i]+n[i+1:])
        
        backtracking([],nums)
        return res
        
                
            
        