class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.cache = {(m-1,n-1):1}
        def dfs(r,c):
            if r >= m or c >= n:
                return 0
            if (r,c) in self.cache:
                return self.cache[(r,c)]
            self.cache[(r,c)] = dfs(r+1,c)
            self.cache[(r,c)] += dfs(r,c+1)
            return self.cache[(r,c)]
        return dfs(0,0)