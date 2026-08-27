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
                self.cache[(i,soFar)] = True
                return self.cache[(i,soFar)]
            if soFar > find:
                self.cache[(i,soFar)] = False
                return self.cache[(i,soFar)]
            if i >= n:
                self.cache[(n,total)] = False
                return False
            l = dfs(i+1,soFar)
            r = dfs(i+1,soFar + nums[i])
            if l or r:
                self.cache[(i,soFar)] = True
            else:
                self.cache[(i,soFar)] = False
            return self.cache[(i,soFar)]
        return dfs(0,0)
