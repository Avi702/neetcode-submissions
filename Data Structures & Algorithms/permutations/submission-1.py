class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i,cur):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            elif i >= len(nums):
                return
            dfs(i+1,cur)
            for j in nums:
                if j not in cur:
                    cur.append(j)
                    dfs(i+1,cur)
                    cur.pop()
        dfs(0,[])
        return ans