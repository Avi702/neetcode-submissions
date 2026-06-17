class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0 
        most = 0
        ans = []
        for R in range(k-1,len(nums)):
            most = max(nums[L:R+1])
            ans.append(most)
            L+=1
        return ans
