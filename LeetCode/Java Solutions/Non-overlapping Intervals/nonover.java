import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        // If the array is null or has no elements, return 0
        if (intervals == null || intervals.length == 0) {
            return 0;
        }

        // Sort the intervals by their end time
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[1] - b[1];
            }
        });

        // Initialize the end time to the first interval's end time
        int end = intervals[0][1];
        int count = 0;

        // Iterate through the intervals starting from the second one
        for (int i = 1; i < intervals.length; i++) {
            // If the current interval's start time is earlier than the last end time, increment the counter
            if (intervals[i][0] < end) {
                count++;
            } else {
                // Otherwise, update the end time
                end = intervals[i][1];
            }
        }

        return count;
    }
}
