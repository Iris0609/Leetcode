## medium
## 52ms, beats 83.33%
## Array
## method 1: layer by layer

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        def spiral_count(r1,r2,c1,c2):
            for c in range(c1,c2+1):
                yield r1,c
            for r in range(r1+1,r2+1):
                yield r,c2
            if r1<r2 and c1<c2:
                for c in range(c2-1,c1-1,-1):
                    yield r2,c
                for r in range(r2-1,r1,-1):
                    yield r,c1
        
        r1,r2=0,len(matrix)-1
        c1,c2=0,len(matrix[0])-1
        ans=[]
        
        while r1<=r2 and c1<=c2:
            for r,c in spiral_count(r1,r2,c1,c2):
                ans.append(matrix[r][c])
            c1+=1
            c2-=1
            r1+=1
            r2-=1
        return ans

## method 2: simulation
## 96ms, beats 0.82%
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        row=len(matrix)
        col=len(matrix[0])
        l=row*col
        # mark whether the item have been add
        simu=[[False]*col for i in range(row)]
        #forward direction
        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        #flag represent the current state
        flag=0
        #ans --result
        ans=[]
        r,c=0,0
        for i in range(l):
            ans.append(matrix[r][c])
            simu[r][c]=True
            rr=r+dr[flag]
            cc=c+dc[flag]
            if 0<=rr<row and 0<=cc<col and not simu[rr][cc]:
                r=rr
                c=cc
            else:
                flag=(flag+1)%4
                r+=dr[flag]
                c+=dc[flag]
        return ans
                
            
 
      