class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def trySpeed(s):
            newPiles = piles
            time = 0
            for bananas in newPiles:
                time += math.ceil(bananas / s)
            return time
        L = 1
        R = max(piles)
        mintime = R
        while L <= R:
            M = (L+R)//2
            time = trySpeed(M)
            if time > h:
                L = M + 1
            elif time <= h:
                mintime = min(M,mintime)
                R = M - 1
        return mintime

