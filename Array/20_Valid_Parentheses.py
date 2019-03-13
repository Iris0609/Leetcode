##easy
##string,stack
##40ms,52.12%
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if not stack:
                    return False
                c=stack.pop()
                if i==')' and c=='(':
                    continue
                elif i=='}' and c=='{':
                    continue
                elif i==']' and c=='[':
                    continue
                else:
                    return False
                
        if len(stack)==0:
            return True
        else:
            return False
                
        