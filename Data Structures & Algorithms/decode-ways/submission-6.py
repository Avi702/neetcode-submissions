class Solution:
    def numDecodings(self, s: str) -> int:
        #bottom-up approach
        n = len(s)
        dp = [1]*(n+1)
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
                continue
            else:
                dp[i] = dp[i+1]
            if i + 1 < n and int(s[i:i+2]) < 27:
                dp[i] += dp[i+2]
        return dp[0]