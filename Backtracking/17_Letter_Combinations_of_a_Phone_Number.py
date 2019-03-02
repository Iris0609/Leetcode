
## medium
##backtracking
## 52ms, 20.37%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        
        def dfs(res,tmp,digits,index):
            if len(tmp)==len(digits):
                res.append(tmp)
                return
            for i in range(index,len(digits)):
                for j in dic[digits[i]]:
                    dfs(res,tmp+j,digits,i+1)
        if not digits:
            return []
        res=[]
        dfs(res,'',digits,0)
        return res
                
            
            
        
#         if not digits:
#             return[]
#         if len(digits)==1:
#             return [i for i in dic[digits[0]]]
        
#         pre=self.letterCombinations(digits[:-1])
#         print(pre)
#         additional=dic[digits[-1]]
#         print(additional)

#         return [s+c for s in pre for c in additional]
            