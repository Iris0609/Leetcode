
## medium
## 56ms, 72.85%
## Array, DP

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path=[[1]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    path[i][j]=path[i-1][j]+path[i][j-1]
                elif i>0 and j==0:
                    path[i][j]=path[i-1][j]
                elif i==0 and j>0:
                    path[i][j]=path[i][j-1]
        return path[-1][-1]

## optimized
## 56ms, 72.85%

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        path=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                path[j]+=path[j-1]
        return path[-1]
