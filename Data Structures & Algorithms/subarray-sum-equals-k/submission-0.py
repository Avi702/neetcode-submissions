class Solution:
    from collections import defaultdict
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            count += prefix[total-k]
            prefix[total] += 1
        return count


            
        




