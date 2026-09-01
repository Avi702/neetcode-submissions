class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        self.cache = {(m,n):0}
        def dfs(i,j):
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            if i == m or j == n:
                self.cache[(i,j)] = 0
                return self.cache[(i,j)]
            if text1[i] == text2[j]:
                res = 1 + dfs(i+1,j+1)
            else:
                res = max(dfs(i+1,j),dfs(i,j+1))
            self.cache[(i,j)] = res
            return self.cache[(i,j)]
        return dfs(0,0)
        