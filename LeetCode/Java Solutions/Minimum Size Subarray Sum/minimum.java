public class Solution {

    // Method that returns the minimum length of a contiguous subarray
    public int minSubArrayLen(int target, int[] nums) {

        // Initialize variables
        int left = 0, right = 0, currSum = 0, minLength = Integer.MAX_VALUE;

        // Iterate through nums with the right pointer
        // Time complexity of this loop is O(n), where n is the size of the input array
        while (right < nums.length) {

            // Add the current value to the running sum
            currSum += nums[right];

            // Check if the current sum is equal or greater than the target
            // In worst case, this inner loop can run n times, so the overall time complexity of this nested loop is O(n)
            while (currSum >= target) {

                // Calculate the length of the current subarray
                int currLength = right - left + 1;

                // Update the minimum length if the current length is smaller
                minLength = Math.min(minLength, currLength);

                // Remove the leftmost value from the running sum and move the left pointer
                currSum -= nums[left];
                left++;
            }

            // Move the right pointer
            right++;
        }

        // Return the minimum length or 0 if no subarray was found
        return minLength != Integer.MAX_VALUE ? minLength : 0;
    }

    // Method to test the solution
    public static void testSolution() {
        Solution s = new Solution();

        assert s.minSubArrayLen(7, new int[]{2, 3, 1, 2, 4, 3}) == 2;
        assert s.minSubArrayLen(4, new int[]{1, 4, 4}) == 1;
        assert s.minSubArrayLen(11, new int[]{1, 1, 1, 1, 1, 1, 1, 1}) == 0;
        assert s.minSubArrayLen(100, new int[]{}) == 0;
        assert s.minSubArrayLen(3, new int[]{1, 1}) == 0;
    }

    public static void main(String[] args) {
        testSolution();
    }
}
