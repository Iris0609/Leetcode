
##hard
##array, stack, two pointer

class Solution:
    def trap(self, height: List[int]) -> int:
        ##brute force
        ##time limit exceeded
        
        tmp=0
        
        for i in range(len(height)):
            max_left=0
            max_right=0
            for j in range(i,-1,-1):
                max_left=max(max_left,height[j])
                
            for h in range(i,len(height)):
                max_right=max(max_right,height[h])
                
            tmp+=min(max_left,max_right)-height[i]
        return tmp
            

##Dynamic Programming
##52ms,52.90%
class Solution:
    def trap(self, height: List[int]) -> int:
        ##brute force
        ##time limit exceeded
        
        if not height:
            return 0
        
        tmp=0
        max_left=[0]*len(height)
        max_left[0]=height[0]
        max_right=[0]*len(height)
        max_right[-1]=height[-1]
        
        for i in range(1,len(height)):
            max_left[i]=max(height[i],max_left[i-1])
        for i in range(len(height)-2,-1,-1):
            max_right[i]=max(height[i],max_right[i+1])
        for i in range(1,len(height)-1):         

            tmp+=min(max_left[i],max_right[i])-height[i]
        return tmp
            
                    
            

            
        