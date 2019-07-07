#easy
#40ms,beats 87.22%

class Solution:
    def countAndSay(self, n: int) -> str:
         
        if n==1:
            return '1'
        if n==2:
            return '11'

        pre='11'
        
        row=3
        while row<=n:
            say=''
            cnt=1
            for i in range(1,len(pre)):
                if pre[i]==pre[i-1]:
                    cnt+=1
                else:
                    say+=str(cnt)+str(pre[i-1])
                    cnt=1
            say+=str(cnt)+str(pre[-1])
            pre=say
            row+=1
            
        return say
            