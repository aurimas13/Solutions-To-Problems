class Solution {
    public int[] getAverages(int[] nums, int k) {
        int n = nums.length;
        int[] result = new int[n];
        long[] prefixSum = new long[n + 1];

        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        for (int i = 0; i < n; i++) {
            if (i - k >= 0 && i + k < n) {
                long sum = prefixSum[i + k + 1] - prefixSum[i - k];
                result[i] = (int)(sum / (2 * k + 1));
            } else {
                result[i] = -1;
            }
        }
        return result;
    }
}
