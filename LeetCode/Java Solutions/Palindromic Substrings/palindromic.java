import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int[] dp = new int[n];
        int[] prev = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(prev, -1);
        int max_size = 1, max_idx = 0;
        
        // Dynamic programming to find the size of the largest subset & reconstructing the subset
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                    if (dp[i] > max_size) {
                        max_size = dp[i];
                        max_idx = i;
                    }
                }
            }
        }
        
        // Reconstruct the largest divisible subset
        List<Integer> subset = new ArrayList<>();
        for (int i = max_idx; i != -1; i = prev[i]) {
            subset.add(0, nums[i]); // Add to the beginning to avoid reversing later
        }
        
        return subset;
    }
}
