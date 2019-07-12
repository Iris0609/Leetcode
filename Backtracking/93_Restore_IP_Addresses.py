#medium
#40ms, 73.93%

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res=[]
        def backtracking(ss,tmp,index):
            if index==4:
                if ss=="":           
                    res.append(tmp[1:])
                return
            
            for i in range(1,4):

                if i<=len(ss):
                    if i==1:
                        backtracking(ss[i:],tmp+"."+ss[:i],index+1)
                    if i==2 and ss[0]!="0":
                        backtracking(ss[i:],tmp+"."+ss[:i],index+1)
                    if i==3 and ss[0]!="0" and ss[:3]<"256":
                        backtracking(ss[i:],tmp+"."+ss[:i],index+1)
                    
            
        backtracking(s,"",0)
        
        return res