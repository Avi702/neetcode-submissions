class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        self.cache = {}
        def dfs(i,j):
            if j >= m:
                return n - i
            if i >= n:
                return m - j
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            if word1[i] == word2[j]:
                count = dfs(i+1,j+1)
            else:
                count = 1 + min(dfs(i,j+1),dfs(i+1,j),dfs(i+1,j+1))
            self.cache[(i,j)] = count
            return self.cache[(i,j)]
        count = dfs(0,0)
        return count
