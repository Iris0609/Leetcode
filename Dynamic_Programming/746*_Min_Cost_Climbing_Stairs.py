## easy
## dp
## 60ms, 28.3%
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        res=[0]*len(cost)
        if len(cost)==0 or len(cost)==1:
            return 0
        res[0]=cost[0]
        res[1]=cost[1]
        
        for i in range(2,len(cost)):
            # way1: from i-2 to i
            tmp1=cost[i]+res[i-2]
            # way 2: from i-1 to i
            tmp2=cost[i]+res[i-1]
            # find the minimum cost way to i
            res[i]=min(tmp1,tmp2)
  
        return min(res[-1],res[-2])


## anothrt way space O(1)
## 44ms, beats 90.57%
class Solution:
    def minCostClimbingStairs(self, cost):
        if len(cost) <= 2: 
            return min(cost)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])

## fastest but hard to understand
## 40ms, beats 100%
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        #reverse to calculate
        for c in cost[::-1]:
            
            f1, f2 = c+min(f1, f2), f1
        
        return min(f1, f2)
        
        