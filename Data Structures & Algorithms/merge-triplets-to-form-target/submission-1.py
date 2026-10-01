class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False, False, False]
        for s, m , e in triplets:
            if s > target[0] or m > target[1] or e > target[2]:
                continue
            good = [s == target[0] or good[0], m == target[1] or good[1], e == target[2] or good[2]]
            if good[0] and good[1] and good[2]:
                return True
        return good[0] and good[1] and good[2]

        