public class Solution {
    private static final int MOD = 1_000_000_007;

    public int countVowelPermutation(int n) {
        long[] previousCount = new long[]{1, 1, 1, 1, 1};

        for (int i = 2; i <= n; i++) {
            long[] currentCount = new long[5];
            // The following transitions are based on the rules defined in the problem.
            currentCount[0] = previousCount[1]; // 'a' can only be followed by 'e'
            currentCount[1] = (previousCount[0] + previousCount[2]) % MOD; // 'e' can be followed by 'a' or 'i'
            currentCount[2] = (previousCount[0] + previousCount[1] + previousCount[3] + previousCount[4]) % MOD; // 'i' can be followed by 'a', 'e', 'o', or 'u'
            currentCount[3] = (previousCount[2] + previousCount[4]) % MOD; // 'o' can be followed by 'i' or 'u'
            currentCount[4] = previousCount[0]; // 'u' can only be followed by 'a'

            previousCount = currentCount;
        }

        long total = 0;
        for (long count : previousCount) {
            total = (total + count) % MOD;
        }

        return (int) total;
    }
}
