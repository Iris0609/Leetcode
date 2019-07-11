
#medium
#32ms,beats95.97%
class Solution:
    def simplifyPath(self, path: str) -> str:
        p=path.split('/')    
        
        if p[-1]=='':
            p.pop()
        pstack=[]
        
        for i in p[1:]:
            if i=='' or i=='.':
                continue  
            elif i=='..':
                if len(pstack)>0:
                    pstack.pop()
                continue
            else:

                pstack.append('/'+i)
                continue

        output='/'+''.join(s for s in pstack)
        op=output.replace('//','/')
        return op