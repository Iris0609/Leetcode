## medium
##backtracking
## 44ms, beats 48.31%
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left=['(']*n
        right=[')']*n
        
        def dfs(res,tmp,left,right):
            if not left and not right:
                res.append(tmp)
                return
            if len(left)>len(right):
                return
            if left:
                dfs(res,tmp+left[-1],left[:-1],right)
            if right:
                dfs(res,tmp+right[-1],left,right[:-1])
            
                
        res=[]
        dfs(res,'',left,right)
        return res