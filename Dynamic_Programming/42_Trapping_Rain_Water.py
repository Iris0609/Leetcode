
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
            
                    
            
        