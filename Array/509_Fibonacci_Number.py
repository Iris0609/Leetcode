## Easy
## Beats 100% 48ms
class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        A=[]
        for i in range(N+1):
            if i==0:
                A.append(0)
            elif i==1:
                A.append(1)
            else:
                A.append(A[-1]+A[-2])
        return A[-1]