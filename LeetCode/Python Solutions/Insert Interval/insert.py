from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result, n = [], len(intervals)
        i = 0
        
        # Skip (and add to output) all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update the newInterval to the merger of it and the current interval
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)  # Add the merged interval
        
        # Add all remaining intervals to the result
        result.extend(intervals[i:])
        
        return result

# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])  # intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]] | intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] -> [[1,2],[3,10],[12,16]]
    print(Solve)


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])  # intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]] | intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] -> [[1,2],[3,10],[12,16]]
    print(Solve)
