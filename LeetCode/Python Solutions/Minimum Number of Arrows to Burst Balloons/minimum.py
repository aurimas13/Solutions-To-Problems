class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort the points based on the end coordinates
        points.sort(key=lambda x: x[1])
        arrows = 0
        arrowPos = float('-inf')
        
        for interval in points:
            # If the current balloon starts after the last arrow position,
            # we need a new arrow
            if interval[0] > arrowPos:
                arrows += 1
                arrowPos = interval[1]  # Update the position to the end of the current balloon
        
        return arrows
