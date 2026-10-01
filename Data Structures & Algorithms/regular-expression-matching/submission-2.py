class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        self.cache = {}
        def dfs(i,j):
            if j == m:
                return i == n
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            first = i < n and (p[j] == s[i] or p[j] == ".")
            if j + 1 < m and p[j+1] == "*":
                res = dfs(i,j+2) or (first and dfs(i+1,j))
            else:
                res = first and dfs(i+1,j+1)
            self.cache[(i,j)] = res
            return self.cache[(i,j)]
        return dfs(0,0)
                
            
                