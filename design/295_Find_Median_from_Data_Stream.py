
##hard
##176ms,58.19%
##using two heap
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.loheap=[]
        self.hiheap=[]
        self.size=0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.loheap,-num)
        heapq.heappush(self.hiheap,-heapq.heappop(self.loheap))
        self.size+=1
        if len(self.loheap)<len(self.hiheap):
            heapq.heappush(self.loheap,-heapq.heappop(self.hiheap))
            
                
    def findMedian(self) -> float:

        if self.size%2==0:
            
            mid=(-self.loheap[0]+self.hiheap[0])/2
            
        else:

            mid=-self.loheap[0]

        return mid


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()