class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if abs(y-x):
                heapq.heappush(stones,-abs(y-x))
        return -stones[0] if stones else 0



        print(stones)
        return 0