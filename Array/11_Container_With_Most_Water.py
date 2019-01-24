## Medium
## 120ms, beats 23.92%
## Tag: Array, Two pointers

## This Solution used two pointers
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0  
        i=0
        j=len(height)-1
        while i<j:
            tmp=min(height[i],height[j])*(j-i)
            max_area=max(tmp,max_area)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return max_area

## A faster solution

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0  
        i=0
        j=len(height)-1
        while i<j:
            tmp=min(height[i],height[j])*(j-i)
            max_area=max(tmp,max_area)
            if height[i]<=height[j]:
                new_i=i+1
                ## if height[new_i] is smaller than height[i], then the area must smaller than now
                ## in this case, we don't need to calculate the new area, just skip
                while height[new_i]<height[i] and new_i<j:
                    new_i+=1
                i=new_i
            else:
                new_j=j-1
                while height[new_j]<height[j] and new_j>i:
                    new_j-=1  
                j=new_j
        return max_area
