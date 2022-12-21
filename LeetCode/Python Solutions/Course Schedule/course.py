import heapq
from typing import List


class Solution:
    @staticmethod
    def scheduleCourse(courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])
        A, curr = [], 0
        for dur, ld in courses:
            heapq.heappush(A, -dur)
            curr += dur
            if curr > ld: curr += heapq.heappop(A)
        return len(A)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.scheduleCourse(courses = [[1,2]])
    # courses = [[3,2],[4,3]] -> 0
    # courses = [[1,2]] -> 1
    print(Solve)
