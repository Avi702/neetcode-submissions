"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        rooms = 0
        end = [i.end for i in intervals]
        start = [i.start for i in intervals]
        end.sort();start.sort()
        e = 0; s = 0;
        while s < len(start):
            if start[s] < end[e]:
                s+=1
                count +=1
            else:
                e += 1
                count -= 1
            rooms = max(count,rooms)
        return rooms
