## Easy
## I failed in many corner case in this problem and fianlly accepted with this prolix code
'''
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3:
            return True
        if A[1]-A[0]<0:
            tmp=-1
        elif A[1]-A[0]==0:
            tmp=0
        else:
            tmp=1

        for i in range(2,len(A)):
            
            if A[i]-A[i-1]<0:
                res=-1
            elif A[i]-A[i-1]==0:
                res=tmp
            else:
                res=1
            if res*tmp<0:
                return False 
            tmp=res
'''
## Here is the code from solution. In this case, we can use 'all' in Python to apply 'compare' to all factor in list.
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return (all(A[i]<=A[i+1] for i in range(len(A)-1)) or all(A[i]>=A[i+1] for i in range(len(A)-1)))
