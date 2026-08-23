class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #top-down approach
        n = len(nums)
        self.cache = {}
        def dfs(i,prev):
            if i >= n:
                return 0
            if (i,prev) in self.cache:
                return self.cache[(i,prev)]
            take = 0
            skip = dfs(i+1,prev)
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i+1,i)
            self.cache[(i,prev)] = max(take,skip)
            return self.cache[(i,prev)]
        return dfs(0,-1)

            