class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = {n:0,n+1:0}
        def dfs(i):
            if i in self.cache:
                return self.cache[i] 
            res = max(nums[i]+dfs(i+2),dfs(i+1))
            self.cache[i] = res
            return self.cache[i]
        return dfs(0)
