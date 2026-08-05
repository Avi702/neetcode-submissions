class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        flip = [(-val,key) for key,val in h.items()]
        heapq.heapify(flip)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(flip)[1])
        return ans



            
            

            