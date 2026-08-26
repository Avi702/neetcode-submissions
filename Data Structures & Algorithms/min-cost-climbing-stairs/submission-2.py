class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.memo = {n:0,n+1:0}
        def dfs(i):
            if i in self.memo:
                return self.memo[i]
            res = min(dfs(i+1),dfs(i+2))
            self.memo[i] = res + cost[i]
            return self.memo[i]
        return min(dfs(0),dfs(1))

