class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
        bucket = [[] for i in range(len(nums)+1)]
        for key,val in h.items():
            bucket[val].append(key)
        ans = []
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans






            
            

            