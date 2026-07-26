class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i,cur,count):
            if count == target:
                ans.append(cur[:])
                return
            if i >= len(nums) or count > target:
                return
            cur.append(nums[i])
            backtrack(i,cur,count + nums[i])
            cur.pop()
            backtrack(i+1,cur,count)
        backtrack(0,[],0)
        return ans