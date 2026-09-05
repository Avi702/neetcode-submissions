class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n - m > 1 or n + m != len(s3):
            return False   
        self.cache = {(n,m):True}
        def dfs(i,j,k):
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            if i < n and j < m and s1[i] == s2[j] == s3[k]:
                self.cache[(i,j)] = bool(dfs(i+1,j,k+1) or dfs(i,j+1,k+1))
            elif i < n and s1[i] == s3[k]:
                self.cache[(i,j)] = dfs(i+1,j,k+1)
            elif j < m and s2[j] == s3[k]:
                self.cache[(i,j)] = dfs(i,j+1,k+1)
            else:
                self.cache[(i,j)] = False
            return self.cache[(i,j)]
        return dfs(0,0,0)
