class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def tryCap(capacity:int,day:int):
            total = 0
            daysTaken = 1
            for weight in weights:
                if total + weight > capacity:
                    daysTaken += 1
                    total = weight
                else:
                    total += weight
            if daysTaken > day:
                return False
            return True
        L = max(weights)
        R = sum(weights)
        mincap = float('inf')
        while L <= R:
            capacity = (L+R)//2
            if tryCap(capacity,days):
                mincap = min(mincap,capacity)
                R = capacity - 1
            else:
                L = capacity + 1
        return mincap


