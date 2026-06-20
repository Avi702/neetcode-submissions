class Solution:
    def findMin(self, nums: List[int]) -> int: 
        n = len(nums)
        R = n - 1
        L = 0
        while L < R:
            M = (L+R)//2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]


        
