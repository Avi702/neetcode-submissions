class Solution:
    from collections import Counter
    import heapq
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for k, v in count.items():
            heap.append([-v,k])
        heapq.heapify(heap)
        if -heap[0][0] > (len(s)+1)//2:
            return ""
        res = []
        prev = None
        while heap:
            c, char = heapq.heappop(heap)
            res.append(char)
            c += 1
            if prev:
                heapq.heappush(heap,prev)
            if c < 0:
                prev = [c,char]
            else:
                prev = None
        return "".join(res)
        