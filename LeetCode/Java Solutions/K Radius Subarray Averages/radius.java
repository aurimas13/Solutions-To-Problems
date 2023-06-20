class Solution {
    public int[] getAverages(int[] nums, int k) {
        int n = nums.length;  // Get the length of nums array
        int[] result = new int[n];  // Initialize the result array with size n
        long[] prefixSum = new long[n + 1];  // Initialize the prefix sum array with size n + 1

        // Generate the prefix sum array
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];  // Update the prefix sum array by adding the current number
        }

        // Calculate the k-radius average for each index
        for (int i = 0; i < n; i++) {
            if (i - k >= 0 && i + k < n) {  // Check if it's possible to create a subarray centered at i with radius k
                long sum = prefixSum[i + k + 1] - prefixSum[i - k];  // Calculate the sum of the subarray
                result[i] = (int)(sum / (2 * k + 1));  // Calculate the average and store it in the result array
            } else {
                result[i] = -1;  // If it's not possible to create such a subarray, assign -1 to the result array
            }
        }
        return result;  // Return the result array
    }
}
