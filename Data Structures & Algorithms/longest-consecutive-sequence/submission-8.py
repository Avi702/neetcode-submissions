class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sset = set(nums)  
        maxcount = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in sset:
                continue
            count = 0
            val = nums[i]
            while val in sset:
                sset.remove(val)
                val += 1
                count += 1
            maxcount = max(maxcount,count)
        return maxcount
            