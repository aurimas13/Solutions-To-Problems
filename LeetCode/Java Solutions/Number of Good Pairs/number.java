import java.util.HashMap;

public class Solution {
    public int numIdenticalPairs(int[] nums) {
        // Use a HashMap to count occurrences of each number
        HashMap<Integer, Integer> numCount = new HashMap<>();
        
        for (int num : nums) {
            numCount.put(num, numCount.getOrDefault(num, 0) + 1);
        }

        // Calculate the number of good pairs
        int count = 0;
        for (int val : numCount.values()) {
            count += (val * (val - 1)) / 2;
        }
        
        return count;
    }
}
