class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        L = 0
        s = Counter(s1)
        h = Counter(s2[:len(s1)])
        if h == s:
            return True
        for R in range(len(s1),len(s2)):
            h[s2[R]] = h.get(s2[R],0) + 1
            L = R - len(s1)
            h[s2[L]] -= 1
            if h[s2[L]] == 0:
                del h[s2[L]]
            if h == s:
                return True
        return False

            
