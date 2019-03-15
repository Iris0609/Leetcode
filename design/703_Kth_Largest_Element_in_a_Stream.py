##easy
##92ms, 51.69%
##heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums=nums
        heapq.heapify(self.nums)
        self.k=k
        while len(self.nums)>k:
            heapq.heappop(self.nums)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)    
        elif val>self.nums[0]:
            heapq.heappush(self.nums,val)
            
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
            
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)