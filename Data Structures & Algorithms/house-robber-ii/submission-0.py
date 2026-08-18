class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRob(nums):
            n = len(nums)
            rob1 = 0
            rob2 = 0
            for i in range(n):
                temp = max(rob1+nums[i],rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(nums[0],houseRob(nums[1:]),houseRob(nums[:-1]))