class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0

        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            # Calculate the differences in x and y coordinates
            deltaX = abs(x2 - x1)
            deltaY = abs(y2 - y1)
            # Add the maximum of these differences to the total time
            totalTime += max(deltaX, deltaY)

        return totalTime
