
#So, backtracking is DFS for implicit tree,
#while DFS is backtracking without pruning. 
#Usually, a depth-first-search is a way of iterating 
#through an actual graph/tree structure looking for a value, 
#whereas backtracking is iterating through a problem space looking for a solution.

## medium
## 152ms, beats 49.04%
## Array, backtracking

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        tmplist=[]
        def backtracking(ind,remain):
            if remain<0:
                return
            elif remain==0:
                # deep copy
                alist=[i for i in tmplist]
                res.append(alist)
            else:
                for i in range(ind,len(candidates)):
                    tmplist.append(candidates[i])
                    backtracking(i,remain-candidates[i])
                    tmplist.pop() #backtracking

        backtracking(0,target)
        return res


## dfs
## 144ms, 56.6%
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        #tmplist=[]
        def backtracking(ind,remain,tmplist):
            if remain<0:
                return
            elif remain==0:
                #alist=[i for i in tmplist]
                res.append(tmplist)
            else:
                for i in range(ind,len(candidates)):
                    #tmplist.append(candidates[i])
                    backtracking(i,remain-candidates[i],tmplist+[candidates[i]])
                    #most difference between dfs and backtracking
                    #tmplist.pop() #backtracking

        backtracking(0,target,[])
        return res