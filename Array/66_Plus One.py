## Easy
## 72ms, beats 17%
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)
        while i>0:
            if digits[i-1]!=9:
                digits[i-1]+=1
                return digits
            else:
                digits[i-1]=0
                i-=1
        if i==0:
            digits=[1]+digits
            return digits

## fastest solution in submission
## change the list into string, then change the string to int. After +1 calculation, change string to list
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        s = ''.join(str(d) for d in digits)
        return list(map(int, str(int(s)+1)))
            