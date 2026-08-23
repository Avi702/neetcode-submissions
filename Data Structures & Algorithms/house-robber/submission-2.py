class Solution:
    def rob(self, nums: List[int]) -> int:
        #top-down memoization
        n = len(nums)
        self.cache = {n:0}
        def dfs(i):
            if i >= n:
                return 0
            if i in self.cache:
                return self.cache[i]
            #take house
            self.cache[i] = max(nums[i]+dfs(i+2),dfs(i+1))
            return self.cache[i]
        return dfs(0)



