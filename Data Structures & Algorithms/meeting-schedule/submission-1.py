"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        starts = {}
        for i in range(1,len(intervals)):
            starts[i] = intervals[i].start
        for i in range(len(intervals)-1):
            if intervals[i].end > starts[i+1]:
                return False

        return True

