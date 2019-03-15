
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        if len(x)<4:
            return False
        
        for i in range(3,len(x)):
            #fourth line crosses first line and onward
            if (x[i]>=x[i-2] and x[i-1]<=x[i-3]):
                return True
            # Fifth line meets first line and onward
            if i>=4 and x[i-1]==x[i-3] and x[i]+x[i-4]>=x[i-2]:
                return True
            # Sixth line meets first line and onward
            if i>=5 and x[i]>=x[i-2]-x[i-4] and x[i-3]-x[i-5]<=x[i-1]<=x[i-3] and x[i-2]>=x[i-4]:
                return True
    
   
                    
                
        return False
            