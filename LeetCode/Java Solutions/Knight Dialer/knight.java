public class Solution {
    public int knightDialer(int n) {
        final int MOD = 1_000_000_007;
        // Possible moves from each digit
        int[][] moves = {
            {4, 6}, {6, 8}, {7, 9}, {4, 8},
            {0, 3, 9}, {}, {0, 1, 7}, {2, 6},
            {1, 3}, {2, 4}
        };

        // Initialize count for each number for length 1
        int[] count = new int[10];
        for (int i = 0; i < 10; i++) {
            count[i] = 1;
        }

        // Dynamic Programming: iterate for length n
        for (int i = 1; i < n; i++) {
            int[] newCount = new int[10];
            for (int num = 0; num < 10; num++) {
                for (int move : moves[num]) {
                    newCount[move] = (newCount[move] + count[num]) % MOD;
                }
            }
            count = newCount;
        }

        // Sum all the counts
        int sum = 0;
        for (int c : count) {
            sum = (sum + c) % MOD;
        }

        return sum;
    }
}
