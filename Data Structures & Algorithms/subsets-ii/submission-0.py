class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def backtrack(i,cur):
            if i == len(nums):
                ans.append(cur[:])
                return
            cur.append(nums[i])
            backtrack(i+1,cur)
            cur.pop()
            new_i = i + 1
            while new_i < len(nums) and nums[new_i] == nums[i]:
                new_i += 1
            backtrack(new_i,cur)
        backtrack(0,[])
        return ans
