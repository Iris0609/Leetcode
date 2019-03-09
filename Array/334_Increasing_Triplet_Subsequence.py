##medium
## array
##44ms 37.31%

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=second=float('Inf')
        
        for i in range(len(nums)):
            if nums[i]<first:
                first=nums[i]
            elif first<nums[i]<second:
                second=nums[i] 
            elif nums[i]>second:
                return True
        return False