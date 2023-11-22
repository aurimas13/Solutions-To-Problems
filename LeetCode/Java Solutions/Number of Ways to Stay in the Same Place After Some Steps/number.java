import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int MOD = 1_000_000_007;
    private Map<String, Integer> memo = new HashMap<>();  // used for memoization

    public int numWays(int steps, int arrLen) {
        return dp(0, steps, arrLen);
    }

    private int dp(int i, int j, int arrLen) {
        // Convert current state to a unique key for memoization
        String key = i + "," + j;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        // Base case
        if (j == 0) {
            return i == 0 ? 1 : 0;
        }
        if (i < 0 || i >= arrLen || i > j) {  // Check out-of-bound and prune unnecessary search
            return 0;
        }

        // Transition: move left, right, or stay
        int left = dp(i - 1, j - 1, arrLen);
        int right = dp(i + 1, j - 1, arrLen);
        int stay = dp(i, j - 1, arrLen);

        // Calculate current state and save to memoization map
        int result = ((left + right) % MOD + stay) % MOD;
        memo.put(key, result);

        return result;
    }
}
