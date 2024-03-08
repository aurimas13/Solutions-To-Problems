import java.util.*;

class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        int maxFreq = 0;
        
        // Count the frequency of each element
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            maxFreq = Math.max(maxFreq, freq.get(num));  // Update the maximum frequency
        }
        
        // Count how many elements have the maximum frequency
        int count = 0;
        for (int key : freq.keySet()) {
            if (freq.get(key) == maxFreq) {
                count += freq.get(key);  // Add the frequency of the element to the count
            }
        }
        
        return count;
    }
}
