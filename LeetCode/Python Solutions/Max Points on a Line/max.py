from typing import List
from collections import defaultdict
from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Function to calculate the slope between two points
        def get_slope(p1, p2):
            # If the x-coordinates are equal, the slope is infinity (vertical line)
            if p1[0] == p2[0]:
                return float('inf')
            # Otherwise, return the slope as a Fraction to avoid floating-point precision issues
            return Fraction(p2[1] - p1[1], p2[0] - p1[0])

        # If the points list is empty, return 0
        if not points:
            return 0
        
        # Initialize the maximum number of points on a line to 0
        max_points = 0
        # Convert the points from lists to tuples
        points = [tuple(point) for point in points]

        # Iterate through the points with index i
        for i in range(len(points)):
            # Create a defaultdict to store the count of points for each slope
            slopes_count = defaultdict(int)
            # Initialize the count of duplicate points to 1
            duplicates = 1

            # Iterate through the remaining points with index j
            for j in range(i + 1, len(points)):
                # If points i and j have the same coordinates, increase the duplicates count
                if points[i] == points[j]:
                    duplicates += 1
                # Otherwise, calculate the slope and increment the count for that slope
                else:
                    slope = get_slope(points[i], points[j])
                    slopes_count[slope] += 1
            
            # Calculate the maximum number of points on the current line by adding duplicates
            max_points_on_line = max(slopes_count.values(), default=0) + duplicates
            # Update the overall maximum points if needed
            max_points = max(max_points, max_points_on_line)

        # Return the overall maximum number of points on a line
        return max_points
    
if __name__ == "__main__":
    # Initialize the Solution class
    solution = Solution()

    # Test case 1
    points1 = [[1, 1], [2, 2], [3, 3]]
    assert solution.maxPoints(points1) == 3, f"Expected 3, but got {solution.maxPoints(points1)}"

    # Test case 2
    points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    assert solution.maxPoints(points2) == 4, f"Expected 4, but got {solution.maxPoints(points2)}"

    # Test case 3
    points3 = [[0, 0], [1, 1], [0, 0]]
    assert solution.maxPoints(points3) == 3, f"Expected 3, but got {solution.maxPoints(points3)}"

    # Test case 4
    points4 = [[0, 0], [1, 65536], [65536, 0], [65536, 65536], [0, 1]]
    assert solution.maxPoints(points4) == 2, f"Expected 2, but got {solution.maxPoints(points4)}"
