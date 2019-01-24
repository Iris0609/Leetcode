## medium
## Array, backtracking
## 52ms, beats 59.4%

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ## sort is necessary here
        nums.sort()
        def dfs(res,tmp,index)
            # difference with subset1
            if not tmp in res:
                res.append(tmp[:])
            for i in range(index,len(nums)):
                tmp.append(nums[i])
                dfs(res,tmp,i+1)
                tmp.pop()

                
  
        dfs(res,[],0)
        return res


## optimize
## 44ms, beats 98.02%
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def dfs(res,tmp,index):
            res.append(tmp[:])
            for i in range(index,len(nums)):
                ##importan: i>index not i>0
                if i>index and nums[i]==nums[i-1]:
                    continue     
                tmp.append(nums[i])
                dfs(res,tmp,i+1)
                tmp.pop()

                
  
        dfs(res,[],0)
        return res