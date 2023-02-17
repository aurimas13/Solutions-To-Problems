from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        """
        Returns the minimum area of a rectangle formed from the given points.

        Parameters:
        points (List[List[int]]): List of n points in the X-Y plane, where points[i] = [xi, yi].

        Returns:
        int: Minimum area of a rectangle formed from the given points, or 0 if no such rectangle exists.
        """
        point_set = set()
        min_area = float('inf')

        for x, y in points:
            for x2, y2 in point_set:
                if x != x2 and y != y2 and (x, y2) in point_set and (x2, y) in point_set:
                    area = abs(x - x2) * abs(y - y2)
                    if area < min_area:
                        min_area = area

            point_set.add((x, y))

        return min_area if min_area != float('inf') else 0


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minAreaRect(points = [[1,1],[1,3],[3,1],[3,3],[2,2]]) 
    # points = [[1,1],[1,3],[3,1],[3,3],[2,2]] -> 4
    # points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]] -> 2
    print(Solve)
