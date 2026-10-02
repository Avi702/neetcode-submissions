class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = []
        for i in range(m):
            cur = []
            for j in range(n+1):
                if j == n:
                    cur.append(float('inf'))
                else:
                    cur.append(grid[i][j])
            dp.append(cur)
        cur = [float('inf')]*(n+1)
        dp.append(cur)
        dp[m][n-1] = 0
        dp[m-1][n] = 0
        print(dp)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] += min(dp[i+1][j],dp[i][j+1])

        return dp[0][0]
        
        