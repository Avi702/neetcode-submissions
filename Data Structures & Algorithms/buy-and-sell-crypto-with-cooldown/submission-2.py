class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        self.cache = {}
        def dfs(i,buy):
            if i >= n:
                return 0
            if (i,buy) in self.cache:
                return self.cache[(i,buy)]
            if buy:
                res = max(dfs(i+1,False)-prices[i],dfs(i+1,True))
            else:
                res = max(dfs(i+2,True)+prices[i],dfs(i+1,False))
            self.cache[(i,buy)] = res
            return self.cache[(i,buy)]
        return dfs(0,True)
