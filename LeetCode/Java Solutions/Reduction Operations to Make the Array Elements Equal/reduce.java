import java.util.Arrays;

class Solution {
    public int reductionOperations(int[] nums) {
        Arrays.sort(nums); // Sort in non-decreasing order
        int operations = 0;
        int distinctCounts = 0;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                distinctCounts++;
            }
            operations += distinctCounts;
        }

        return operations;
    }
}
