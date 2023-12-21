from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract the x-coordinates and sort them.
        x_coords = sorted(point[0] for point in points)

        # Initialize the maximum width to 0.
        max_width = 0

        # Iterate through the sorted x-coordinates.
        for i in range(1, len(x_coords)):
            # Calculate the difference between consecutive x-coordinates.
            width = x_coords[i] - x_coords[i - 1]

            # Update the maximum width if the current width is greater.
            max_width = max(max_width, width)

        return max_width
