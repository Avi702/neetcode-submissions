class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev = float('-inf')
        erase = 0
        for s, e in intervals:
            if s < prev:
                erase+=1
            else:
                prev = e
        return erase
            
