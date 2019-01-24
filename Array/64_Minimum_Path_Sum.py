## medium
## 78ms, beats 38.08%
## Array, Dynamic Programming
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        row=len(grid)
        col=len(grid[0])
        if row==1 or col==1:
            s=0
            for r in range(row):
                for c in range(col):
                    s+=grid[r][c]
            return s
        
        path=[[0]*col for r in range(row)]
        
        
        for r in range(row):
            for c in range(col):
                if r>0 and c>0:
                    path[r][c]=grid[r][c]+min(path[r-1][c],path[r][c-1])
                elif r==0 and c==0:
                    path[r][c]=grid[r][c]
                elif r==0 and c>0:
                    path[r][c]=grid[r][c]+path[r][c-1]
                elif c==0 and r>0:
                    path[r][c]=grid[r][c]+path[r-1][c]
                    
        return path[-1][-1]

## clear solution and no extra space
## 64ms, beats 58.75%
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        row=len(grid)
        col=len(grid[0])

        for r in range(1,row):
            grid[r][0]=grid[r][0]+grid[r-1][0]
        for c in range(1,col):
            grid[0][c]=grid[0][c]+grid[0][c-1]
        
        
        for r in range(1,row):
            for c in range(1,col):
                    grid[r][c]=grid[r][c]+min(grid[r-1][c],grid[r][c-1])
        return grid[-1][-1]
        



        