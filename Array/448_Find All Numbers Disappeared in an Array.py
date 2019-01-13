## Easy
## limited O(n) and no extra space
## 284ms, beats 48.5%
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
        return [i+1 for i in range(len(nums)) if nums[i]>0]


## fastest solution in leetcode submission
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setNums = set(nums) ## no extra space???
        ans = []
        for i in range(len(nums)):
            i += 1
            if i not in setNums:
                ans.append(i)
        return ans
