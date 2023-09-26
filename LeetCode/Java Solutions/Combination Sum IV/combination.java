import java.util.Arrays;

public class Solution {
    public static int combinationSum4(int[] nums, int target) {
        Arrays.sort(nums);

        // Notice that we cap the size of our circular dp array by max(nums)+1
        int dpSize = Math.min(target, getMax(nums)) + 1;
        int[] dp = new int[dpSize];
        dp[0] = 1;

        // We need to skip comb_sum == 0 since that's a special seed value and
        // we don't want to clear it in the next line
        for (int comb_sum = 1; comb_sum <= target; comb_sum++) {
            // We need to clear entries to prevent carry-over of old values
            dp[comb_sum % dpSize] = 0;

            for (int num : nums) {
                if (comb_sum - num >= 0) {
                    // We use modular arithmetic for indexing since our dp array is circular
                    dp[comb_sum % dpSize] += dp[(comb_sum - num) % dpSize];
                } else {
                    break;
                }
            }
        }

        return dp[target % dpSize];
    }

    private static int getMax(int[] nums) {
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        int target = 4;
        int result = combinationSum4(nums, target);
        System.out.println(result);  // Expected output: 7
    }
}
