##medium
##48ms, 93.94%

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        ob=2147483647
        l=0
        lefte=reader.get(l)
        r=abs(target)+abs(lefte)
        while l<r:

            lefte=reader.get(l)
            righte=reader.get(r)
            mid=(l+r)//2
            mide=reader.get(mid)
            if lefte==target:
                return l
            if righte==target:
                return r
            if target<lefte:
                return -1
            if mide==target:
                return mid
            # print(l,mid,r)
            if mid==l:
                return -1
            if lefte<target<mide:
                r=mid-1
            elif mide<target<righte:
                l=mid+1
            
        return -1
        
        