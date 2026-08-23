class Solution:
    def numDecodings(self, s: str) -> int:
        #bottom-up approach
        n = len(s)
        dp = dp2 = 0
        dp1 = 1
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
                if i + 1 < n and int(s[i:i+2]) < 27:
                    dp += dp2
            dp,dp1,dp2 = 0,dp,dp1
        return dp1