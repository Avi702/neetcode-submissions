class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(cur,open_i,close_i):
            if len(cur) == 2*n:
                ans.append(cur[:])
                return
            if close_i < open_i:
                backtrack(cur + ")",open_i,close_i+1)
            if open_i < n:
                backtrack(cur + "(",open_i+1,close_i)
        backtrack("",0,0)
        return ans