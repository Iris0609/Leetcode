## medium 
## 56ms, beats 98.88%
## tricky method in python, using list index function
## binary search, array
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
 
        if not target in nums:
            return -1
        else:
            return nums.index(target)


## solution, complex and slow.
## 88ms, beats 7.04%
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        def find_rotate_index(i,j):
            # rotate_index dones not exist
            if nums[i]<nums[j]:
                return 0
            # find pivot
            while i<=j:
                mid=(i+j)//2
                
                if nums[mid]>nums[mid+1]:
                    return mid+1             
                else:
                    if nums[mid]<nums[mid-1] and mid>0:
                        return mid
                    if nums[i]<nums[mid]:
                        i=mid+1
                    else:
                        j=mid-1
 
        
        def search(i,j):
            #binary search target
            while i<=j:
                mid=(i+j)//2
                if target==nums[mid]:
                    return mid
                elif target<nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
        
            return -1
        
        rotate_index=find_rotate_index(0,len(nums)-1)
        
        # if target is the smallest element
        if target==nums[rotate_index]:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index==0:
            return search(0,len(nums)-1)
        if target>=nums[0]:
            # search on the left side
            return search(0,rotate_index-1)
        else:
            # search on the right side
            return search(rotate_index+1,len(nums)-1)


        
        
                
            

## fastest solution in submission
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        if nums[0] == target:
            return 0
        
        # find the pivot point
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            if nums[left] > nums[mid]:
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 
            else:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

