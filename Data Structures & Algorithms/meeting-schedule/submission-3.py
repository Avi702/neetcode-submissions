"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval = sorted(intervals, key = lambda x: x.start)
        for i in range(len(intervals)):
            if i > 0 and (interval[i-1].start <= interval[i].start < interval[i-1].end or interval[i-1].start <= interval[i].end < interval[i-1].end):
                return False
        return True
