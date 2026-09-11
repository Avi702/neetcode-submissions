class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        self.cache = {}
        def dfs(left,right):
            if left > right:
                return 0
            if (left,right) in self.cache:
                return self.cache[(left,right)]
            best = 0
            for k in range(left,right+1):
                best = max(best,dfs(left,k-1)+nums[left-1]*nums[k]*nums[right+1]+dfs(k+1,right))
            self.cache[(left,right)] = best
            return best
        return dfs(1,n-2)