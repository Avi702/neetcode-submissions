class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        def dfs(res,sset):
            if len(res) == n:
                ans.append(res[:])
                return
            for j in range(n):
                if j > 0 and nums[j] == nums[j-1] and (j-1) not in sset:
                    continue
                if j not in sset:
                    sset.add(j)
                    res.append(nums[j])
                    dfs(res,sset)
                    sset.remove(j)
                    res.pop()
        dfs([],set())
        return ans
