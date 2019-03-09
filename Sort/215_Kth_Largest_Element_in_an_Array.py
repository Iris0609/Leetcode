##44ms, beats 64.12%

class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##maximum heap
        # n=[-nums[i] for i in range(len(nums))]
        # heapq.heapify(n)       
        # for i in range(k-1):
        #     heapq.heappop(n)
        # return -heapq.heappop(n)
        
## 52ms, beats 44.79%
        ## minimum heap
        ini=[-float('inf')]*k
        heapq.heapify(nums)
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(nums,ini[i])
            heapq.heappop(nums)
        return heapq.heappop(nums)
