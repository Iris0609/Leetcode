## medium
## 72ms, beats 90.49%
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n=len(nums)-1
        l=n-1
        ## find the first pair nums[l]<nums[n] from right
        while l>=0:
            if nums[l]<nums[n]:
                break
            else:
                n-=1
                l=n-1
        if n==0:
            ## if the whole list is descending, reverse the list
            nums.reverse()
        
        elif n>0:
            ## find the item while just larger than nums[l] from the right side (nums[l+1:])
            nl=nums[l]
            diff=2**30
            for i in range(l+1,len(nums)):
                ## find the item while just larger than nums[l] from the right side (nums[l+1:])
                if nums[i]-nl>0 and nums[i]-nl<diff:
                    n=i
            # swap 
            nums[l],nums[n]=nums[n],nums[l]
            # reversed the right side (nums[l+1:])         
            nums[l+1:]=nums[:l:-1]

## Optimize
## 68ms, beats 98.84%
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n=len(nums)-1
        l=n-1
        while l>=0:
            if nums[l]<nums[n]:
                break
            else:
                n-=1
                l=n-1
        if n==0:
            nums.reverse()
        
        elif n>0:
            ## Here if we count from the right, the first larger item is the just larger item.
            for i in range(len(nums)-1,l,-1):
                if nums[l]<nums[i]:
                    n=i
                    break
            nums[l],nums[n]=nums[n],nums[l]         
            nums[l+1:]=nums[:l:-1]
        
                