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
        max_rooms,rooms,j = 1,1,0
        end = ends[j]
        for i in range(1,len(intervals)):
            if starts[i] < end:
                rooms += 1
                max_rooms = max(max_rooms,rooms)
            else:
                j += 1
                end = ends[j]
        return max_rooms