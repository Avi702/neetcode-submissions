class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1]*(n+2)
        dp[0] = 0
        for i in range(1,n+2):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]