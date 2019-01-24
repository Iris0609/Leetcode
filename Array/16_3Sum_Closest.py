## medium
## 136ms, beats 92.45%
## Array, Two pointers
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_diff=100000000000
        tmp=0
        nums.sort()
        if len(nums)<4:
            return sum(nums)
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: continue
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[r]+nums[l]
                diff=abs(target-s)
                if diff<min_diff:
                    min_diff=diff
                    tmp=s
                if s==target:
                    return target
                elif s>target:
                    r-=1
                    while l<r and nums[r]==nums[r+1]: r-=1
                else:
                    l+=1
                    while l<r and nums[l]==nums[l-1]:l+=1
        return tmp
        