class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        stack = []
        erase = 0
        for s, e in intervals:
            if stack and s < stack[-1][1]:
                erase+=1
                if stack[-1][1] > e:
                    stack[-1] = [s,e]
            else:
                stack.append([s,e])
        return erase
            
