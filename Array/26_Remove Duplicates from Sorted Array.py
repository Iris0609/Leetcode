## Easy
## 136ms, beats 24.75%
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=1
        if len(nums)==0:
            return 0
        while i<len(nums):
            if nums[i]>nums[i-1]:
                i+=1
            else:
                nums.pop(i)
        return i

            