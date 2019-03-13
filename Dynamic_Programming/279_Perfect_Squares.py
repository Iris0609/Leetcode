
##medium
##dp
## 5520ms beats 22.34%
class Solution:
    def numSquares(self, n: int) -> int:
        ##dp
        dp=[n]*(n+1)
        dp[0]=0
        dp[1]=1
        
        #if we can find a j, j*j is a perfect square, cnt+1
        # res=dp[i]+dp[j*j]=dp[i]+1
        for i in range(1,n+1):
            j=1
            local_res=i
            while i-j*j>=0:
                local_res=min(dp[i-j*j]+1,local_res)
                j+=1
            dp[i]=local_res
        
        return dp[n]
        

            
## bfs
## 240ms 74.46%
import math
class Solution:
    def numSquares(self, n: int) -> int:
        ##bfs
        tmpres=[n]
        cnt=0
        cal_list=[]
        for i in range(1,int(math.sqrt(n))+1):
            cal_list.append(i*i)
        
        while(tmpres):
            locallist=set()
            cnt+=1
            for i in tmpres:  
                for j in cal_list:
                    if i==j: return cnt
                    if i-j<0: break
                    locallist.add(i-j)
                    
            tmpres=list(locallist)