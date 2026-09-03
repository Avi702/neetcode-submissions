class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}
        def dfs(total,i):
            if i >= len(nums):
                if total == target:
                    return 1
                return 0
            if (total,i) in self.cache:
                return self.cache[(total,i)]
            l = dfs(total + nums[i], i+1)
            r = dfs(total - nums[i], i + 1)
            self.cache[(total,i)] = l + r
            return self.cache[(total,i)]
        return dfs(0,0)