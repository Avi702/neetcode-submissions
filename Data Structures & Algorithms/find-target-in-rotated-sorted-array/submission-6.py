class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            M = (L+R)//2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        min_i = R
        if min_i == 0:
            L = 0; R = len(nums) - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            L = 0; R = min_i - 1
        else:
            L = min_i; R = len(nums) - 1
        while L <= R:
            M = (L+R)//2
            if nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
            else:
                return M
        return -1
