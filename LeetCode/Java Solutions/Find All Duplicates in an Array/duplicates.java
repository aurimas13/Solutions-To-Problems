import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> duplicates = new ArrayList<>();
        for (int num : nums) {
            // Use Math.abs to handle negation
            int index = Math.abs(num) - 1;
            if (nums[index] < 0) {
                // If the value at index is negative, we've seen this number before
                duplicates.add(Math.abs(num));
            } else {
                // Negate the value at index to mark num as seen
                nums[index] = -nums[index];
            }
        }
        return duplicates;
    }
}
