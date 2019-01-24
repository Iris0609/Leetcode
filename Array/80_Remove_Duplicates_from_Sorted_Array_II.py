## medium
## 76ms, beats 26.64%


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            if i>1 and nums[i]==nums[i-2]:
                nums.pop(i)
            else:
                i+=1
    return i

## genius solution in discussion
## 44ms, beats 100%
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for n in nums:
            #if n greater than nums[i-1], make sure duplicates appeared at most twice
            if i<2 or n>nums[i-2]:
                nums[i]=n
                i+=1

        return i