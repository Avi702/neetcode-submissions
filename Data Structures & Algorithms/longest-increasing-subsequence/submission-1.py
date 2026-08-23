class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #top-down approach
        n = len(nums)
        self.cache = {}
        def dfs(i):
            if i in self.cache:
                return self.cache[i]
            best = 1
            for k in range(i+1,n):
                if nums[k] > nums[i]:
                    best = max(1+dfs(k),best)
            self.cache[i] = best
            return best
        res = 1
        for num in range(n):
            res = max(res,dfs(num))
        return res
                

            