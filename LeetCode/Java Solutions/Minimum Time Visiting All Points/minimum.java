public class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int totalTime = 0;

        for (int i = 0; i < points.length - 1; i++) {
            int[] point1 = points[i];
            int[] point2 = points[i + 1];

            // Calculate the differences in x and y coordinates
            int deltaX = Math.abs(point2[0] - point1[0]);
            int deltaY = Math.abs(point2[1] - point1[1]);

            // The time to move between these two points is the maximum of deltaX and deltaY
            totalTime += Math.max(deltaX, deltaY);
        }

        return totalTime;
    }
}
