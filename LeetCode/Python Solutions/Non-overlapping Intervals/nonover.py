from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # If the list is empty, return 0
        if not intervals:
            return 0

        # Sort the intervals by their end time
        intervals.sort(key=lambda x: x[1])

        # Initialize the end time to the first interval's end time
        end = intervals[0][1]
        count = 0

        # Iterate through the intervals starting from the second one
        for i in range(1, len(intervals)):
            # If the current interval's start time is earlier than the last end time, increment the counter
            if intervals[i][0] < end:
                count += 1
            else:
                # Otherwise, update the end time
                end = intervals[i][1]

        return count
