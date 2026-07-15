class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(len(prices)):
            while prices[R] - prices[L] < 0 and L<=R:
                L+=1
            profit = max(prices[R] - prices[L],profit)
        return profit


            
            
            