class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = {}
        def dfs(i):
            if i == n:
                return 0
            if i in self.cache:
                return self.cache[i]
            self.cache[i] = max(dfs(i+1) + nums[i],nums[i])
            return self.cache[i]
        res = float('-inf')
        for i in range(n):
            res = max(dfs(i),res)
        return res
            
            

        
        