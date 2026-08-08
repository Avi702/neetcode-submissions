class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        interval = sorted(intervals, key = lambda x:x[0])
        for i in interval:
            if stack and (stack[-1][0] <= i[0] <= stack[-1][1] or stack[-1][0] <= i[1] <= stack[-1][1]):
                s, e = stack.pop()
                stack.append([min(s,i[0]),max(e,i[1])])
            else:
                stack.append(i)
        return stack
