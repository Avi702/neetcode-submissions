class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.cache = {}
        def dfs(remaining,i):
            if (remaining, i) in self.cache:
                return self.cache[(remaining,i)]
            if remaining < 0 or i >= len(coins):
                return 0
            if remaining == 0:
                return 1
            l = dfs(remaining-coins[i],i)
            r = dfs(remaining,i+1)
            self.cache[(remaining,i)] = l + r
            return self.cache[(remaining,i)]
        return dfs(amount,0)