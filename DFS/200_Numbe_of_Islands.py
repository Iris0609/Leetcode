##medium
##80ms,57.82%
##dfs


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.row=len(grid)
        self.col=len(grid[0])
        
        def dfs(r,c,grid):
            if r<0 or r>=self.row or c<0 or c>=self.col or grid[r][c]!='1':
                return
            grid[r][c]='*'
            dfs(r+1,c,grid)
            dfs(r-1,c,grid)
            dfs(r,c+1,grid)
            dfs(r,c-1,grid)
  
        cnt=0
        
        for r in range(self.row):
            for c in range(self.col):
                if grid[r][c]=='1':
                    dfs(r,c,grid)
                    cnt+=1
 
        return cnt