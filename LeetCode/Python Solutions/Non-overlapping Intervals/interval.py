from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by finish time
        intervals.sort(key= lambda x: x[1])
        dp = [1]* len(intervals)
        prev = intervals[0]
        for i in range(1, len(dp)):
            if prev[1] > intervals[i][0]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
                prev = intervals[i]

        return len(intervals) - dp[len(intervals)-1]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]])  # intervals = [[1,2],[1,2],[1,2]] -> 2
    print(Solve)