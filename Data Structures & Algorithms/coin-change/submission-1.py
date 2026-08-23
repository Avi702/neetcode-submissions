class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        self.cache = {0:0}

        def dfs(remaining):
            res = float('inf')
            if remaining < 0:
                return res
            if remaining in self.cache:
                return self.cache[remaining]
            for c in coins:
                res = min(res,1+ dfs(remaining-c))
            self.cache[remaining] = res
            return res
        ans = dfs(amount)
        if ans == float('inf'):
            return -1
        return ans

            