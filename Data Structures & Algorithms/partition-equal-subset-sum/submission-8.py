class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        n = len(nums)
        find = total // 2
        self.cache = {(n,total): False}
        def dfs(i,target):
            if (i,target) in self.cache:
                return self.cache[(i,target)]
            if target == 0:
                return True
            if target < 0 or i >= n:
                return False
            self.cache[(i,target)] = dfs(i+1,target) or dfs(i+1,target-nums[i])
            return self.cache[(i,target)]
        return dfs(0,find)
