class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkCapacity(capacity: int, weights: List[int]):
            total = 0
            day = 1
            for i in weights:
                if total + i > capacity:
                    day += 1
                    total = i
                else:
                    total += i
            if day > days:
                return False
            return True
        cap =0
        L = max(weights); R = sum(weights)
        while L <= R:
            M = (L+R)//2
            if checkCapacity(M,weights):
                cap = M
                R = M - 1
            else:
                L = M + 1
        return cap



