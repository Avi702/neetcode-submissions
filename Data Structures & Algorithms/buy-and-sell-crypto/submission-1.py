class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0
        for R in range(len(prices)):
            while prices[L] > prices[R] and L<=R:
                L+=1
            profit = max(prices[R] - prices[L],profit)
        return profit


            
            
            