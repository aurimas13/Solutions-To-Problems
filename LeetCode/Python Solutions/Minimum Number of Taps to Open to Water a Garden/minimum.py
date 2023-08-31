from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxRange = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            maxRange[left] = max(maxRange[left], right)
        
        # Greedy approach
        start, end, taps = 0, 0, 0
        while end < n:
            start, end = end, max(maxRange[i] for i in range(start, end + 1))
            if start == end:
                return -1
            taps += 1
        return taps

