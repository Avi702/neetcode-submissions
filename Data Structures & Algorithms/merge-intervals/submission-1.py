class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        interval = sorted(intervals, key = lambda x: x[0])
        for i in interval:
            if stack and i[0] <= stack[-1][1]:
                k, j = stack.pop()
                stack.append([min(k,i[0]),max(j,i[1])])
            else:
                stack.append(i)
        return stack
