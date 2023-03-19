from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert each time point to minutes using list comprehension
        minutes = sorted([int(tp[:2]) * 60 + int(tp[3:]) for tp in timePoints])

        # Calculate differences between consecutive time points and append the difference between first and last time points
        diffs = [minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1)] + [1440 - minutes[-1] + minutes[0]]

        # Return the minimum difference
        return min(diffs)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findMinDifference(timePoints = ["23:59","00:00"])
    # timePoints = ["23:59","00:00"] -> 1
    # timePoints = ["00:00","23:59","00:00"] -> 0
    print(Solve)
