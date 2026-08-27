class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        n = len(nums)
        find = total // 2
        self.cache = {(n,total): False}
        def dfs(i,soFar):
            if (i,soFar) in self.cache:
                return self.cache[(i,soFar)]
            if soFar == find:
                return True
            if soFar > find or i >= n:
                return False
            res = dfs(i+1,soFar) or dfs(i+1,soFar+nums[i])
            self.cache[(i,soFar)] = res
            return res
        return dfs(0,0)
