class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(cur):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for j in nums:
                if j not in cur:
                    cur.append(j)
                    dfs(cur)
                    cur.pop()
        dfs([])
        return ans