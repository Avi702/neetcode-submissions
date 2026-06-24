class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        if len(nums) < 4:
            return ans
        if len(nums) == 4 and sum(nums) != target:
            return ans
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j> i+1 and nums[j] == nums[j-1]:
                    continue
                L = j + 1; R = len(nums)-1
                while L < R:
                    total = nums[i] + nums[j] + nums[L] + nums[R]
                    if total == target:
                        ans.append([nums[i],nums[j],nums[L],nums[R]])
                        L += 1; R-=1
                        while L < R and nums[L] == nums[L-1]:
                            L +=1
                        while L < R and nums[R] == nums[R+1]:
                            R -=1
                    elif total > target:
                        R -= 1
                    else:
                        L +=1
        return ans








