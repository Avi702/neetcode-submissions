class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack = []
        for index , i in enumerate(temperatures):
            while stack and stack[-1][1]<i:
                w,j=stack.pop()
                ans[w]=index-w

            stack.append((index,i))

        return ans


