public class Solution {
    public long minimumReplacement(int[] nums) {
        // Initialize the operations counter using long data type
        long operations = 0;
        
        // Start with the last number in the list as the boundary.
        // Convert to long for calculation.
        long currentBoundary = nums[nums.length - 1];

        // Loop through the list in reverse (excluding the last element since it's our boundary).
        for (int i = nums.length - 2; i >= 0; i--) {
            // Calculate how many times we'd have to split 'num' 
            // to make its parts smaller than the currentBoundary.
            // Use long for intermediate calculations.
            long splitCount = (long)nums[i] + currentBoundary - 1;
            splitCount /= currentBoundary;
            
            // Update the operations needed.
            operations += splitCount - 1;
            
            // Update the currentBoundary.
            currentBoundary = (long)nums[i] / splitCount;
        }

        return operations;
    }
}
