class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float('inf')
        L = 0; total = 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                min_l = min(min_l,R-L+1)
                total -= nums[L]
                L+=1
        if min_l == float('inf'):
            return 0
        return min_l
