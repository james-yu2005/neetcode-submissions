"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        i = 0
        j = 0
        start = [0] * len(intervals)
        end = [0] * len(intervals)
        for k in range(len(intervals)):
            start[k] = intervals[k].start
        for k in range(len(intervals)):
            end[k] = intervals[k].end
        start.sort()
        end.sort()
        max_meet = 0
        meeting = 0
        while i < len(intervals):
            if start[i] < end[j]:
                meeting += 1
                max_meet = max(meeting, max_meet)
                i += 1
            else:
                meeting -= 1
                j += 1
        
        return max_meet




