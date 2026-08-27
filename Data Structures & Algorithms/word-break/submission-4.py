class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sset = set(wordDict)
        self.memo = {"":True}
        def dfs(sub):
            if sub in self.memo:
                return self.memo[sub]
            for c in range(1,len(sub)+1):
                if sub[:c] in sset:
                    self.memo[sub] = dfs(sub[c:])
                    if self.memo[sub]:
                        return True
            self.memo[sub] = False
            return False
        return dfs(s)
                