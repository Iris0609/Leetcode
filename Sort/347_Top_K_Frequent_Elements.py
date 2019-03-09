
## medium


##60ms, 36.06%
##defaultdict is faster than dic

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic=collections.defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]]+=1

        
        bucket=[[] for _ in range(len(nums)+1)]
        for key,v in dic.items():
            bucket[v].append(key)
        
        res=[]
        for row in reversed(bucket):
            if not row:
                continue
            else:
                for col in row:
                    res.append(col)
                    if len(res)==k:
                        return res
##72ms, 21.49%

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=dic.setdefault(nums[i],1)+1
            
        l=sorted(dic.items(),key=lambda item: item[1],reverse=True)[:k]
        return [i[0] for i in l ]