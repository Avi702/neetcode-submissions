class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        s = sorted(s1)
        for R in range(len(s1)-1,len(s2)):
            print(s2[L:R+1])
            if sorted(s2[L:R+1]) == s:
                return True
            L += 1
        return False

            
