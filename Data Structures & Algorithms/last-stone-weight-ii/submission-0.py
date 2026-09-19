class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        self.cache = {}
        def dfs(i,s):
            if i == n:
                return abs(s - (total - s))
            if (i,s) in self.cache:
                return self.cache[(i,s)]
            self.cache[(i,s)] = min(dfs(i+1,s),dfs(i+1,s+stones[i]))
            return self.cache[(i,s)]
        return dfs(0,0)
            



