class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur,curSet):
            if len(nums) == len(cur):
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if i not in curSet:
                    cur.append(nums[i])
                    curSet.add(i)
                    backtrack(cur,curSet)
                    cur.pop()
                    curSet.remove(i)
        backtrack([],set())
        return ans
            