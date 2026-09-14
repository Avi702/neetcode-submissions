class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur):
            if len(nums) == len(cur):
                ans.append(cur[:])
                return
            for i in nums:
                if i not in cur:
                    cur.append(i)
                    backtrack(cur)
                    cur.pop()
        backtrack([])
        return ans
            