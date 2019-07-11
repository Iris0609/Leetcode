
## easy
##40ms, 80.01%
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x<=3:
            return 1
        
        def bisearch(l,r):
            mid=(l+r)//2
            if (l*l==x) or (l*l<x and (l+1)*(l+1)>x):
                return l
            if (r*r==x) or (r*r<x and (r+1)*(r+1)>x):
                return r
            if (mid*mid==x) or (mid*mid<x and (mid+1)*(mid+1)>x):
                return mid
            if mid*mid>x:
                return bisearch(l,mid)
            else:
                return bisearch(mid,r)      
            
        res=bisearch(0,x//2)
        print(res)
        return res



    ###method2: simple math
    r = x
    while r*r > x:
        r = (r + x/r) / 2
    return r