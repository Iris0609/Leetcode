

##medium
##64ms, 57.89%
##stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            cur=asteroids[i]
            while cur<0:
                if stack and stack[-1]>0:
                    tmp=stack.pop()
                    if abs(cur)<tmp:
                        cur=tmp
                    elif abs(cur)==tmp:
                         break                     
                else:
                    stack.append(cur)
                    break
            if cur>0:
                stack.append(cur)
            
        return stack
            
 