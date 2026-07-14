"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # need to sort the array with the first value - [(0,30),(5,10),(15,20)]
        from typing import List
        sorted_meetings = sorted(intervals, key=lambda x: x.start)

        # to make sure to attend a meeting, end time of ith meeting should be before the start time of the (i+1)th meeting or else we can flag 
        for i in range(1, len(sorted_meetings)):
            if sorted_meetings[i].start < sorted_meetings[i-1].end:
                # there is overlap
                return False

        return True

