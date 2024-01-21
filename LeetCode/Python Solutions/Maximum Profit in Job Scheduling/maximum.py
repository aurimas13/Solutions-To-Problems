from typing import List
from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0, 0)]  # (endTime, profit) pair, initial dummy job with 0 profit

        for start, end, profit in jobs:
            # Find the last job that ends before the current job starts
            i = bisect_left(dp, (start, float('inf'))) - 1
            if dp[i][1] + profit > dp[-1][1]:
                # If this job plus the best previous job is better than the last best job
                dp.append((end, dp[i][1] + profit))

        return dp[-1][1]
