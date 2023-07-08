import java.util.Arrays;

class Solution {
    /**
     * Calculates the difference between the maximum and minimum sums of pairs of adjacent weights
     * given an array of weights and the number of pairs to consider.
     *
     * @param  weights  the array of weights
     * @param  k        the number of pairs to consider
     * @return          the difference between the maximum and minimum sums of pairs
     */
    public long putMarbles(int[] weights, int k) {
        if (k == 1 || k == weights.length) {
            return 0;
        }
        
        long[] sortedPairs = new long[weights.length - 1];
        for (int i = 0; i < weights.length - 1; i++) {
            sortedPairs[i] = (long)weights[i] + weights[i + 1];
        }
        
        Arrays.sort(sortedPairs);
        
        long maxSum = 0;
        long minSum = 0;
        for (int i = sortedPairs.length - k + 1; i < sortedPairs.length; i++) {
            maxSum += sortedPairs[i];
        }
        for (int i = 0; i < k - 1; i++) {
            minSum += sortedPairs[i];
        }
        
        return maxSum - minSum;
    }
}

