class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = n - 1
            target = -nums[i]
            while L < R:
                total = nums[L] + nums[R]
                if total == target:
                    ans.append([nums[i],nums[L],nums[R]])
                    L += 1; R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                elif total < target:
                    L += 1
                else:
                    R -= 1
        return ans
                