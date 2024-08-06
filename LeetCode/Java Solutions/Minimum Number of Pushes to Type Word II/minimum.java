class Solution {
    public int findMinArrowShots(int[][] points) {
        // Sort the points based on the end coordinates
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        int arrows = 0;
        long arrowPos = Long.MIN_VALUE; // Use long to avoid overflow issues
        
        for (int[] interval : points) {
            // If the current balloon starts after the last arrow position,
            // we need a new arrow
            if (interval[0] > arrowPos) {
                arrows++;
                arrowPos = interval[1]; // Update the position to the end of the current balloon
            }
        }
        
        return arrows;
    }
}
