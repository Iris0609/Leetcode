## midium
## math, string

class Solution:  
    def myAtoi(self, str: str) -> int:
        def is_number(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        
        
        ws=False
        negative=None
        first=False
        res=''
        for i in str:
            # white space
            if i==" " and first==False:
                if ws==False:
                    continue
                else:
                    break
            elif i==" " and first==True:
                break
            # minus   
            if i=="-" and first==False:
                first=True
                if negative==None:
                    res+=i
                    negative=True
                    continue
                else:
                    break
            elif i=="-" and first==True:
                break
                
            # plus
            if i=="+" and first==False:
                first=True
                if negative==None:
                    negative=False
                    continue
                else:
                    break
            elif i=="+" and first==True:
                break
            
            if is_number(i):
                first=True
                res+=i
                continue
            else:
                break
                
        if not res:
            return 0
        if not is_number(res):
            return 0
            
                
        if int(res)>=2**31:
            res=2**31-1
        elif int(res)<=-2**31:
            res=-2**31
        else:
            res=int(res)
        return res
                
            
            