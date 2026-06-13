class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = len(nums)-1
        R = 0
        while L > R:
            total = nums[R]+nums[L]
            if total == target:
                return [R+1,L+1]
            elif total > target:
                L-=1
            elif total < target:
                R+=1


        





