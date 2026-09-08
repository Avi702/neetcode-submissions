class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        count = 0
        i = 0
        while True:
            jump = nums[i]
            count += 1
            if i + jump >= n - 1:
                return count
            maxjump = 0
            start = i + 1
            for j in range(start,start + jump):
                if j + nums[j] > maxjump:
                    i = j
                    maxjump = nums[j]    
