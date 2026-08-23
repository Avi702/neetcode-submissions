class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom-up -> O(1) space
        n = len(nums)
        temp = 0; rob1 = 0; rob2 = 0
        for i in range(n-1,-1,-1):
            temp = max(rob1+nums[i],rob2)
            rob1 = rob2
            rob2 = temp
        return rob2



