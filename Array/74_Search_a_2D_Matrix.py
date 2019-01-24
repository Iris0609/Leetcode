## Medium
## 60ms, beats 94.12%
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=len(matrix)
        if row==0:
            return False
        col=len(matrix[0])
        i=0
        j=col-1
        while i<row and j>=0:
            if target<matrix[i][j]:
                j-=1
            elif target>matrix[i][j]:
                i+=1
            else:
                return True
        return False


## fastest solution in submission
## binary search
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m,n=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif target>matrix[mid//n][mid%n]:
                l=mid+1
            else:
                r=mid-1
        return False