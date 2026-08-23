class Solution:
    def numDecodings(self, s: str) -> int:
        #top-down approach
        n = len(s)
        self.cache = {n:1,n+1:1}
        def dfs(i):
            if i in self.cache:
                return self.cache[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if i + 1 < n and int(s[i:i+2]) < 27:
                res += dfs(i+2)
            self.cache[i] = res
            return res
        return dfs(0)
        