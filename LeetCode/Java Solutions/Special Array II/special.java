class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;

        // Handle edge case: if nums has only one element, all subarrays are special
        if (n == 1) {
            boolean[] result = new boolean[queries.length];
            for (int i = 0; i < queries.length; i++) {
                result[i] = true;
            }
            return result;
        }

        // Precompute parity differences
        int[] parityDiff = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            parityDiff[i] = (nums[i] % 2 != nums[i + 1] % 2) ? 1 : 0;
        }

        // Compute prefix sums
        int[] prefix = new int[n - 1];
        prefix[0] = parityDiff[0];
        for (int i = 1; i < n - 1; i++) {
            prefix[i] = prefix[i - 1] + parityDiff[i];
        }

        // Answer queries
        boolean[] result = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int fromi = queries[i][0];
            int toi = queries[i][1];

            if (toi == fromi) { // Single element case
                result[i] = true;
            } else {
                int totalDiff = prefix[toi - 1] - (fromi > 0 ? prefix[fromi - 1] : 0);
                result[i] = (totalDiff == (toi - fromi));
            }
        }

        return result;
    }
}
