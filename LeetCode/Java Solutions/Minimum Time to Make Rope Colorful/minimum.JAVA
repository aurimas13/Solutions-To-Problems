public class Solution {
    public int minCost(String colors, int[] neededTime) {
        int total_time = 0;
        int max_time = 0;  // Track the maximum time in the current group of same-colored balloons.
        int current_time = 0;  // Track the total time for the current group.

        for (int i = 0; i < colors.length(); i++) {
            if (i > 0 && colors.charAt(i) != colors.charAt(i - 1)) {
                // If the color changes, add the total time of the previous group minus the max time.
                total_time += current_time - max_time;
                // Reset the max_time and current_time for the new group.
                max_time = 0;
                current_time = 0;
            }
            
            // Update the current and max times.
            current_time += neededTime[i];
            max_time = Math.max(max_time, neededTime[i]);
        }
        
        // Add the time for the last group of balloons.
        total_time += current_time - max_time;
        
        return total_time;
    }
}
