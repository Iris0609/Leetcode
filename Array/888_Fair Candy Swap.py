## Easy
## 5176ms, beats 12.03%
class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ad=(sum(A)-sum(B))//2
        res=[]

        for i in A:
            if i-ad in B:
                res.append(i)
                res.append(i-ad)
                return res
## O(n^2) if don't use set(B), plus the time in list append. Slow.
## When use set(B), O(len(A)+len(B))

## 96ms, beats 99.25%


class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ad=(sum(A)-sum(B))//2
        setB=set(B)

        for i in A:
            if i-ad in setB:
                return [i,i-ad]

        