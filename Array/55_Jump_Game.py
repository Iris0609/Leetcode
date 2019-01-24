
## medium
## 64ms, beats 95.75%

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not 0 in nums:
            return True
        
        for i in range(len(nums)-1):
            if nums[i]==0:
                ind=i-1
                while ind>=0:
                    if nums[ind]>i-ind:
                        break
                    else:
                        ind-=1
                if ind>=0:
                    continue
                else:
                    return False
        return True