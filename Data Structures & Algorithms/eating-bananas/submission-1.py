class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        R = max(piles)
        L = 1
        min_s = R
        while L <= R:
            total = 0
            k = (L+R) // 2
            for i in range(len(piles)):
                total += (piles[i] + k - 1)//k
            if total > h:
                L = k + 1
            elif total <= h:
                R = k - 1
                min_s = min(min_s,k)
        return min_s
            
            



                
            

        




