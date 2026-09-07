class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        self.cache = {}
        def dfs(i,j):
            if j == n:
                return 1
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            res = 0
            for k in range(i,m):
                if s[k] == t[j]:
                    res += dfs(k+1,j+1)
            self.cache[(i,j)] = res
            return self.cache[(i,j)]
        val = dfs(0,0)
        print(self.cache)
        return val