class Solution:
    def climbStairs(self, n: int) -> int:
        h = {n:1, n+1:0}
        def dfs(i):
            if i in h:
                return h[i]
            one = dfs(i+1)
            two = dfs(i+2)
            h[i] = one + two
            return h[i]
        return dfs(0)