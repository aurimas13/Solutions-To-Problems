from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Create bloom events
        events = []
        for start, end in flowers:
            events.append((start, 1))  # Bloom starts
            events.append((end + 1, -1))  # Bloom ends

        # Sort events by time
        events.sort()

        # Calculate flowers in bloom at each event
        bloom_count = 0
        bloom_at_time = {}
        for time, change in events:
            bloom_count += change
            bloom_at_time[time] = bloom_count

        # For each person, find how many flowers are blooming at their arrival time
        res = []
        for time in people:
            # Use binary search to find the closest event time <= person's arrival
            index = self.binary_search(events, time)
            if index == -1:
                res.append(0)
            else:
                closest_event_time = events[index][0]
                res.append(bloom_at_time[closest_event_time])
        return res

    def binary_search(self, events, time):
        """Find the index of the closest event time <= given time."""
        left, right = 0, len(events) - 1
        while left <= right:
            mid = (left + right) // 2
            if events[mid][0] <= time:
                left = mid + 1
            else:
                right = mid - 1
        return right if right >= 0 else -1
