from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.canAttendMeetings([[7,10],[2,4]])  # intervals = [[7,10],[2,4]] -> true | [[0,30],[5,10],[15,20]] -> false
    print(Solve)