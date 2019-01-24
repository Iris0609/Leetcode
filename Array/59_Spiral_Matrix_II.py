## medium
## 56ms, beats 90.51%

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return [[]]
        
        matrix=[[0]*n for i in range(n)]
        flag=1
        
        # This function is used to decide the row and col of the next order
        def generate(r1,r2,c1,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2
            if r1<r2 and c1<c2:
                for c in range(c2-1,c1-1,-1):   
                    yield(r2,c)
                for r in range(r2-1,r1,-1):
                    yield(r,c1)
        
        r1,r2=0,n-1
        c1,c2=0,n-1
        # both is okay
        # while r1<=r2 and c1<=c2:  
        while flag<=n*n:
            for r,c in generate(r1,r2,c1,c2):
                matrix[r][c]=flag
                flag+=1
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return matrix
            
            
                
                
        