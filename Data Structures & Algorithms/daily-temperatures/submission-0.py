class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for index,i in enumerate(temperatures):
            while stack and stack[-1][0] < i:
                s_t, s_i = stack.pop()
                ans[s_i] = index - s_i
            stack.append((i,index))
        return ans







            
        return s
