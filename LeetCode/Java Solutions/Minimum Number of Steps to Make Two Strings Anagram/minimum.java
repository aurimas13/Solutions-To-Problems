import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minOperations(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        int operations = 0;

        // Count the occurrences of each number
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        for (int count : freq.values()) {
            // If exactly one occurrence, impossible to remove it
            if (count == 1) {
                return -1;
            }

            // 'Three elements removal' operations
            operations += count / 3;
            
            // If there's a remainder, one more operation is needed
            if (count % 3 != 0) {
                operations += 1;
            }
        }

        return operations;
    }
}
