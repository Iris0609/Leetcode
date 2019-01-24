## medium
## 36ms, beats 99.84%
## insertion sort, array

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


        for i in range(1,len(nums)):
            curval=nums[i]
            curind=i
            while curind>0 and nums[curind-1]>curval:
                nums[curind]=nums[curind-1]
                curind-=1
            nums[curind]=curval
                
## One pass solution
class Solution:
    def sortColors(self,nums):
        red,white,blue=0,0,len(nums)-1
        while white<=blue:
            if nums[white]==0:
                nums[red],nums[white]=nums[white],nums[red]
                red+=1
                white+=1
            elif nums[white]==1:
                white+=1
            else:
                nums[white],nums[blue]=nums[blue],nums[white]
                blue-=1

                    
                    
