class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i,cur,count):
            if count == target:
                res.append(cur[:])
                return
            if i >= len(nums) or count > target:
                return
            next_i = i + 1
            while next_i < len(nums) and nums[i] == nums[next_i]:
                next_i+=1
            backtrack(next_i,cur,count)
            cur.append(nums[i])
            backtrack(i+1,cur,count+nums[i])
            cur.pop()
        backtrack(0,[],0)
        return res