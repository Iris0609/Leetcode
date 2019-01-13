## Easy
## 64ms,beats 35.15%
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]<target:
                i+=1
            else:
                return i
        return i

## Using for loop will be faster
## 56ms, beats 88.9%
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)