class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()
        ans = []
        for R in range(len(nums)):
            while dq and dq[0] <= R - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[R]:
                dq.pop()
            dq.append(R)
            if R >= k-1:
                ans.append(nums[dq[0]])
        return ans
