class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort the events by start time
        events.sort(key=lambda x: x[0])

        # Initialize a dictionary to keep track of the maximum value for each number of events
        dp = {}

        # Define a helper function to find the maximum value for each number of events
        def helper(i, k):
            # If we have visited this event before, return the maximum value for this number of events
            if (i, k) in dp:
                return dp[(i, k)]

            # If we have reached the end of the events, return 0
            if i == len(events):
                return 0

            # If we have no more events to attend, return 0
            if k == 0:
                return 0

            # If we have to skip this event, move on to the next event
            if events[i][1] <= events[i][0]:
                return helper(i + 1, k)

            # If we have to attend this event, move on to the next event
            if k == 1:
                return events[i][2] + helper(i + 1, k)

            # If we have to attend this event, move on to the next event
            # Else, we can either attend this event or skip this event
            dp[(i, k)] = max(events[i][2] + helper(i + 1, k), helper(i + 1, k - 1))
            return dp[(i, k)]

        # Return the maximum value for k events
        return helper(0, k)
