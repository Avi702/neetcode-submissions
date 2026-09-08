class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        j = n - 1
        for i in range(n-2,-1,-1):
            if j - i <= nums[i]:
                j = i
        return j == 0
            
