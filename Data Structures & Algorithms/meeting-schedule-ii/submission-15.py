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
        days = 1
        intervals = sorted(intervals, key=lambda x:x.start)
        heap = []
        heapq.heappush(heap,intervals[0].end)
        for itvl in intervals[1:]:
            if itvl.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,itvl.end)
            days = max(days,len(heap))
        return days