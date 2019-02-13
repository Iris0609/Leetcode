## easy
## dp
## 44ms, 93.9%

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)):
            if i>0:
                nums[i]=max(nums[i],nums[i]+nums[i-1])
        return max(nums)
