#medium
##32ms, beats 92.3
## bit manipulate
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        absdivisor=abs(divisor)
        absdividend=abs(dividend)
        
        cnt=0
        res=absdividend
        shift=31
        while shift>=0:
            if absdividend>=absdivisor<<shift:
                #<<shift=2**shift
                absdividend-=absdivisor<<shift
                cnt+=1<<shift
            shift-=1

        if (divisor<0 and dividend>0) or (divisor>0 and dividend<0):
            cnt=-cnt
            return cnt
        else:
            return cnt if cnt<2**31 else 2**31-1
        