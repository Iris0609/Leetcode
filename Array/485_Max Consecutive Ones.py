## Easy
## 100ms, beats 95.87%

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp=0
        last=-1
        for i,item in enumerate(nums):
            if item==0:
                res=i-last-1
                last=i
                if res>tmp:
                    tmp=res
        a=len(nums)-last-1
        return max(tmp,a)