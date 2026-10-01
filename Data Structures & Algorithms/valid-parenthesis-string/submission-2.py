class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        for i in s:
            if i == ')':
                lo = max(0,lo-1) 
                hi -= 1
            elif i == '(':
                lo += 1
                hi += 1
            else:
                lo = max(0,lo-1) 
                hi += 1
            if hi < 0:
                return False
        return lo == 0


        
                
                    


