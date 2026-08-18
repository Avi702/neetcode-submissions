"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [s.start for s in intervals]
        end = [e.end for e in intervals]
        start.sort(); end.sort()
        n = len(end)
        rooms = 0
        maxrooms = 0
        s = 0; e = 0
        while s < n:
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            maxrooms = max(maxrooms,rooms)
        return maxrooms