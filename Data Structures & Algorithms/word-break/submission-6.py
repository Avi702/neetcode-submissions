class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sset = set(wordDict)
        n = len(s)
        self.memo = {n:True}
        def dfs(i):
            if i in self.memo:
                return self.memo[i]
            for j in range(i,n+1):
                if s[i:j+1] in sset:
                    self.memo[i] = dfs(j+1)
                    if self.memo[i]:
                        return True
            self.memo[i] = False
            return False
        return dfs(0)
                