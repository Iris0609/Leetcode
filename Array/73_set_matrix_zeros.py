## medium
## Array
## 132ms, beats 31.97%
## too slow. O(m*n)

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        zerocol=[]
        zerorow=[]
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c]==0:
                    zerorow.append(r)
                    zerocol.append(c)
        
        for r in range(row):
            for c in range(col):
                if r in zerorow or c in zerocol:
                    matrix[r][c]=0