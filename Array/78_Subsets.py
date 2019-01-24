## medium
## backtracking, array
## 36ms, beats 100%

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(res,tmp,index):
            res.append(tmp[:])# deep copy of tmp
            for i in range(index,len(nums)):
                tmp.append(nums[i])
                dfs(res,tmp,i+1)
                tmp.pop()
        
        dfs(res,[],0)
        return res

## Another structure
## 44ms, 56.16%

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(res, tmp, index):
            res.append(tmp)
            for i in range(index, len(nums)):
                dfs(res,tmp+[nums[i]],i+1)
        
        dfs(res,[],0)
        return res
