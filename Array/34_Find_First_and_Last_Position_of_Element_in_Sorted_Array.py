## medium
## 60ms, beats 93.41%
## Array, binary search

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1,-1]
        if not nums:
            return res
            
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                l=mid
                r=mid
                while l>0 and nums[l]==nums[l-1]:l-=1
                while r<len(nums)-1 and nums[r]==nums[r+1]:r+=1
                return [l,r]
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return res
            
            