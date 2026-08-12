class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memory = {n: 0}
        def dfs(i):
            if i >= n:
                return 0
            if i + 1 not in memory:
                memory[i+1] = dfs(i+1)
            l = memory[i + 1]
            if i + 2 not in memory:
                memory[i+2] = dfs(i+2)
            r = memory[i+2]
            return cost[i] + min(l,r)
        return min(dfs(0),dfs(1))
        