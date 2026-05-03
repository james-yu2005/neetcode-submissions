"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x:x.end)
        curr_end = intervals[0].end
        for itvl in intervals[1:]:
            if curr_end <= itvl.start:
                curr_end = itvl.end
            else:
                return False
        return True