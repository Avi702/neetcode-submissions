class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        L = 0
        s = sorted(s1)
        for R in range(len(s1)-1,len(s2)):
            if s != sorted(s2[L:R+1]):
                L+=1
                continue
            return True
        return False

            


