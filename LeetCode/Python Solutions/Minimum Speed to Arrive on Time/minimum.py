from typing import List
from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # Initialize the low and high speed
        # low speed = 1 and high speed is maximum distance multiply by 10^7 to ensure cover maximum possible speed
        low, high = 1, max(dist) * int(1e7)
        
        # If number of trains is greater than hour and hour is not integer
        # Then it's impossible to reach at time.
        if len(dist) > ceil(hour):
            return -1

        # Binary search for minimum speed
        while low < high:
            mid = (low + high) // 2  # Find the middle speed
            time = sum(ceil(d / mid) for d in dist[:-1]) + dist[-1] / mid  # Calculate the total time with middle speed
            if time > hour:  # If the total time is more than given hour then increase the low speed
                low = mid + 1
            else:  # Else reduce the high speed
                high = mid
        return low
