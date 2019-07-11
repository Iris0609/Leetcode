
#medium
#704ms, beats 27.49%

##using backtracking, slow
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]
        def backtracking(tmp,li):
            if len(tmp)==k:
                res.append(tmp)
                return
             
            for i in range(len(li)):
                backtracking(tmp+[li[i]],li[i+1:])
            
        li=[l for l in range(1,n+1)]
        backtracking([],li)
        return res

#optimize backtracking
#620ms, beats 52%
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]
        def backtracking(tmp,pos):
            if len(tmp)==k:
                res.append(tmp)
                return
             
            for i in range(pos,n+1):
                backtracking(tmp+[i],i+1)
            
        backtracking([],1)
        return res

# optimize again
#124ms, beats3.33%

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]
        def backtracking(k,res,tmp,pos):
            if k==0:
                res.append(tmp)
                return
             
            for i in range(pos,n+1):
            ##important for speeding! filer those cannot get len(tmp)=k
                if n - i + 1 < k:
                     return
            ##
                backtracking(k-1,res,tmp+[i],i+1)
            
        backtracking(k,res,[],1)
        return res

