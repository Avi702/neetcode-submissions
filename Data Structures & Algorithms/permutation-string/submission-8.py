class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        L = 0
        s = Counter(s1)
        for R in range(len(s1)-1,len(s2)):
            h = Counter(s2[L:R+1])
            if h == s:
                return True
            L += 1
        return False

            
