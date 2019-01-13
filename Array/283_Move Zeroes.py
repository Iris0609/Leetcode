## Easy
## 72ms, beats 80.61%
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while i<len(nums):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
            i+=1
