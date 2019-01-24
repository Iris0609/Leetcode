
# medium
# 92ms, 82.87%
# Array, sort


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res=[]
        intervals.sort(key=lambda x: x.start)

        
        for i in range(len(intervals)):
            if not res or res[-1].end<intervals[i].start:
                res.append(intervals[i])
            else:
                res[-1].end=max(intervals[i].end,res[-1].end)

            

        return res
                
                
                

                