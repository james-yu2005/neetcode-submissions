"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        starts = sorted([time.start for time in intervals])
        ends = sorted([time.end for time in intervals])
        max_rooms,rooms,s,e = 0,0,0,0
        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                rooms += 1
            else:
                e += 1
                rooms -= 1
            max_rooms = max(rooms,max_rooms)
        return max_rooms