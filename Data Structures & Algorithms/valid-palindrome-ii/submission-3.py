class Solution:
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        delete1 = 0
        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            elif delete1 == 0:
                R-=1
                delete1 += 1
            else:
                delete1 += 1
                break
        if delete1 < 2:
            return True
        delete2 = 0
        L = 0; R = len(s)-1
        while L <= R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            elif not delete2:
                L+=1
                delete2 += 1
            else:
                delete2 += 1
                break
        return delete2 < 2
        
        
        
            
            