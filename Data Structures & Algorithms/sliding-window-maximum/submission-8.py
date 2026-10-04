class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        R = 0
        res = []
        while R < k:
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)
            R+=1
        res.append(nums[q[0]])
        L = 0
        for i in range(k,len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            if q and q[0] < L + 1:
                q.popleft()
            q.append(i)
            L += 1
            res.append(nums[q[0]])
        return res
        