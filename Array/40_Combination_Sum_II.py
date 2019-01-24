## medium
## 84ms, beats 81.14%
## Array, backtracking

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        #tmplist=[]
        candidates.sort()
        def dfs(remain,ind,tmplist):
            if remain==0:
                res.append(tmplist)
                #return
            else:
                for i in range(ind,len(candidates)):
                    if i > ind and candidates[i]==candidates[i-1]:
                        continue
                    if candidates[i]>remain:
                        break
                    dfs(remain-candidates[i],i+1,tmplist+[candidates[i]])
                    
        dfs(target,0,[])
        return res
            
            
            