## Easy
## 72ms, beats 11.35%
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        A=[[1],[1,1]]
        for i in range(2,numRows):
            tmp=[1]*(i+1)
            for j in range(1,i):
                    tmp[j]=A[i-1][j-1]+A[i-1][j]
            A.append(tmp)
        return A


## fastest in submission
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        L=[1]
        res=[]
        for n in range(1,numRows+1):
            res.append(L)
            L=[1]+[L[i]+L[i+1]for i in range(len(L)-1)]+[1]
        return res

