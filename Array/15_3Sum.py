## Medium
##1304ms, beats 73.32%
## Tag: Array, Two pointers
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        if j<2:
            return []
        for i in range(len(nums)-2):
            ## remove duplicate i
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    #remove duplicate l
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    # remove duplicate r
                    while l<r and nums[r+1]==nums[r]:
                        r-=1
                elif s>0:
                    r-=1
                else:
                    l+=1
                
                    
        return res
        #return list(set([tuple(t) for t in res]))



                
            
            
        