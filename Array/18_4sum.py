##medium
## 1904ms, beats 9.98%
##Array, two pointers, Hash Table
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        if len(nums)<4:
            return res
        if len(nums)==4 and sum(nums)==target:
            return [nums]
        
        
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for l in range(i+1,len(nums)-2):  
                if l>i+1 and nums[l-1]==nums[l]: 
                    continue
                m=l+1
                r=len(nums)-1

                while m<r:
                    s=nums[i]+nums[l]+nums[m]+nums[r]
                    if s==target:
                        res.append([nums[i],nums[l],nums[m],nums[r]])
                        m+=1
                        r-=1
                        while m<r and nums[m]==nums[m-1]: m+=1
                        while m<r and nums[r]==nums[r+1]: r-=1
                    elif s>target:
                        r-=1
                    else:
                        m+=1
        return res



## Fastest solution in submission, using recursive
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums,target,N,result,results):
            ## corner case
            if N<2 or len(nums)<N or nums[0]*N>target or nums[-1]*N < target:
                return
            ## two sum
            if N==2:
                l=0
                r=len(nums)-1
                while l<r:
                    s=nums[l]+nums[r]
                    if s==target:
                        results.append(result+[nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif s<target:
                        l+=1
                    else:
                        r-=1
            else:
                # when N>2, decompose the question to 2sum by update nums, target and N
                for i in range(len(nums)-N+1):
                    if i==0 or (i>0 and nums[i]!=nums[i-1]):
                        findNsum(nums[i+1::],target-nums[i],N-1,result+[nums[i]],results)
        results = []
        result = []
        findNsum(sorted(nums), target,4,result,results)
        return results
        
        
        