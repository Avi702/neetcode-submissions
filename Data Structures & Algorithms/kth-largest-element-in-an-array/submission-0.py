class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums) #O(n)
        for j in range(k-1):
            heapq.heappop(nums)
        return -nums[0]

        
