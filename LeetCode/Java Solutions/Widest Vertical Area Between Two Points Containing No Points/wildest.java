import java.util.*;

class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        // Extract the x-coordinates and sort them.
        int[] xCoords = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            xCoords[i] = points[i][0];
        }
        Arrays.sort(xCoords);

        // Initialize the maximum width to 0.
        int maxWidth = 0;

        // Iterate through the sorted x-coordinates.
        for (int i = 1; i < xCoords.length; i++) {
            // Calculate the difference between consecutive x-coordinates.
            int width = xCoords[i] - xCoords[i - 1];

            // Update the maximum width if the current width is greater.
            maxWidth = Math.max(maxWidth, width);
        }

        return maxWidth;
    }
}
