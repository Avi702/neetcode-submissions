class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while stones:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
                if x < y or x > y:
                    heapq.heappush(stones,-abs(y-x))
            else:
                return -x
        return 0
