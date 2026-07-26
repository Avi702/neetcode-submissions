class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            profit = max(prices[R] - prices[L],profit)
        return profit


            
            
            