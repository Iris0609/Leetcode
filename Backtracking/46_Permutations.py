## medium
## 56ms, beats 42.12%

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums,tmp,res):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],tmp+[nums[i]],res)
                
        res=[]
        dfs(nums,[],res)
        return res
                