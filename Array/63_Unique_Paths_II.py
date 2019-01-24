## medium
## 60ms, 68.02%
## Array, dynamic programming

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        
        path=[[0]*col for i in range(row)]
        
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    path[i][j]=1-obstacleGrid[i][j]
                    if i==0 and j>0:
                        path[i][j]=min(1-obstacleGrid[i][j],path[i][j-1])
                    if j==0 and i>0:
                        path[i][j]=min(1-obstacleGrid[i][j],path[i-1][j])
                else:
                    path[i][j]=(path[i-1][j]*(1-obstacleGrid[i-1][j])+path[i][j-1]*(1-obstacleGrid[i][j-1]))*(1-obstacleGrid[i][j])
        return path[-1][-1]
                    