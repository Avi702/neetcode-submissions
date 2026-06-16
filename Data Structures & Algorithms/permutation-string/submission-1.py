class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        for R in range(len(s1)-1,len(s2)):
            if sorted(s1) != sorted(s2[L:R+1]):
                L+=1
                continue
            return True
        return False

            


