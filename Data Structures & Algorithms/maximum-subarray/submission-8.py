class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = {}
        def dfs(i):
            if i >= n:
                return 0
            if i in self.cache:
                return self.cache[i]
            self.cache[i] = max(nums[i],dfs(i+1)+nums[i])
            return self.cache[i]
        return max(dfs(i) for i in range(n))
