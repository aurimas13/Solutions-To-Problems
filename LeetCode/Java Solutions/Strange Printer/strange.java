class Solution {
    int[][] memo; // This array is used to memoize results of subproblems

    public int strangePrinter(String s) {
        int n = s.length();
        memo = new int[n][n]; // Initialize the memo array
        return dp(s, 0, n - 1); // Call the function with the full string
    }

    private int dp(String s, int i, int j) {
        if (i > j) return 0; // If the start of the substring is after its end, it's an empty substring, so the printer needs 0 turns
        if (memo[i][j] == 0) { // If this subproblem has not been solved before
            int ans = dp(s, i + 1, j) + 1; // The printer will need at least one more turn than the optimal solution for the substring that doesn't include the first character
            for (int k = i + 1; k <= j; k++) { // For every possible ending of the substring
                if (s.charAt(k) == s.charAt(i)) { // If the character at the ending is the same as the character at the beginning
                    // It might be better to print them together
                    ans = Math.min(ans, dp(s, i, k - 1) + dp(s, k + 1, j)); // The printer will need the minimum number of turns between the current best and the new option
                }
            }
            memo[i][j] = ans; // The result is stored in the memo array
        }
        return memo[i][j]; // The result is returned
    }
}
