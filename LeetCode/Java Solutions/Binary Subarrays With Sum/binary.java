import java.util.HashMap;

class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        HashMap<Integer, Integer> prefixSumCount = new HashMap<>();  // Map to store count of prefix sums
        int runningSum = 0;
        int count = 0;
        
        for (int num : nums) {
            // Increment the running sum
            runningSum += num;
            // If runningSum equals goal, increment count
            if (runningSum == goal) {
                count++;
            }
            // Add to count the number of times (runningSum - goal) has occurred
            count += prefixSumCount.getOrDefault(runningSum - goal, 0);
            // Increment the count of runningSum in the map
            prefixSumCount.put(runningSum, prefixSumCount.getOrDefault(runningSum, 0) + 1);
        }
        
        return count;
    }
}


