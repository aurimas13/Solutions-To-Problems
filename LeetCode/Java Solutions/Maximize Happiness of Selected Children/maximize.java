import java.util.Arrays;

public class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        // Sort the happiness array in descending order
        Arrays.sort(happiness);
        // Reverse the array to make it descending
        for (int i = 0; i < happiness.length / 2; i++) {
            int temp = happiness[i];
            happiness[i] = happiness[happiness.length - 1 - i];
            happiness[happiness.length - 1 - i] = temp;
        }
        
        long maxSum = 0;
        // Calculate the maximum sum by taking the top k elements
        for (int i = 0; i < k; i++) {
            maxSum += Math.max(0, happiness[i] - i);
        }
        
        return maxSum;
    }
}
