##352ms beats 56.78%
##medium
##sliding window, two pointer


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(set(tree))<=2:
            return len(tree)
        
        dic={}# track fruit type: value
        
        start=0
        end=0
        res=0
        tmpres=0
        
        while end<len(tree):
            
            tmpres+=1
            if tree[end] not in dic:
                dic[tree[end]]=1
            else:
                dic[tree[end]]+=1
                
            if len(dic)>2:
                dic[tree[start]]-=1
                if dic[tree[start]]==0:
                    del dic[tree[start]]
                tmpres-=1
                start+=1
            end+=1
            res=max(res,tmpres)
            
        return res
            
        
                
                
                    
