import java.util.*;

class Solution {
    // Define a method that takes a 2D array of events and an integer k as inputs
    public int maxValue(int[][] events, int k) {
        // Sort the events array by the end times
        Arrays.sort(events, Comparator.comparingInt(a -> a[1]));

        // Initialize endTimeAndValuePairs to store pairs of [endTime, totalValue]
        List<int[]> endTimeAndValuePairs = new ArrayList<>();
        // The first pair [0, 0] represents the initial state where no event is attended
        endTimeAndValuePairs.add(new int[]{0, 0});

        // Initialize newEndTimeAndValuePairs to store pairs for the next round
        List<int[]> newEndTimeAndValuePairs = new ArrayList<>();
        newEndTimeAndValuePairs.add(new int[]{0, 0});

        // Iterate over each attended event
        for (int attendedEventCount = 0; attendedEventCount < k; attendedEventCount++) {
            for (int[] event : events) {
                // For each event, get start time, end time and value
                int start = event[0], end = event[1], value = event[2];

                // Find the event in endTimeAndValuePairs whose end time is less than the start time of the current event
                int indexOfEvent = Collections.binarySearch(endTimeAndValuePairs, new int[]{start, 0}, Comparator.comparingInt(a -> a[0]));
                if (indexOfEvent < 0) {
                    indexOfEvent = -indexOfEvent - 2;
                }

                // If the total value by attending the current event is larger than the last total value in newEndTimeAndValuePairs
                // Append this new pair to newEndTimeAndValuePairs
                if (indexOfEvent != -1 && endTimeAndValuePairs.get(indexOfEvent)[1] + value > newEndTimeAndValuePairs.get(newEndTimeAndValuePairs.size() - 1)[1]) {
                    newEndTimeAndValuePairs.add(new int[]{end, endTimeAndValuePairs.get(indexOfEvent)[1] + value});
                }
            }

            // Update endTimeAndValuePairs with newEndTimeAndValuePairs for the next round
            endTimeAndValuePairs = new ArrayList<>(newEndTimeAndValuePairs);
            // Reset newEndTimeAndValuePairs for the next round
            newEndTimeAndValuePairs = new ArrayList<>();
            newEndTimeAndValuePairs.add(new int[]{0, 0});
        }

        // Return the maximum value which is the last value in endTimeAndValuePairs
        return endTimeAndValuePairs.get(endTimeAndValuePairs.size() - 1)[1];
    }
}
