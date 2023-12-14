import java.math.BigInteger;

class Solution {
    private static final BigInteger M = BigInteger.valueOf(10).pow(9).add(BigInteger.valueOf(7));  // Modulus to prevent overflow
    private BigInteger[][][] memo;  // Memoization array to store previously computed results

    public int numMusicPlaylists(int n, int goal, int k) {
        memo = new BigInteger[n + 1][goal + 1][k + 1];
        return numMusicPlaylistsHelper(n, goal, k).intValue();
    }

    private BigInteger numMusicPlaylistsHelper(int n, int goal, int k) {
        if (n == 0 || n <= k) {
            return BigInteger.ZERO;  // If there are no songs or the number of songs is less than or equal to k, return 0
        }
        if (n == 1) {
            return BigInteger.ONE;  // If there is only one song, return 1
        }
        if (memo[n][goal][k] != null) {
            return memo[n][goal][k];  // If the result is already computed, return it
        }

        BigInteger result = BigInteger.valueOf(n);  // Initialize result to n

        // Calculate all the combinations, including those that do not include every song
        for (int i = 1; i < goal; i++) {
            if (i <= k) {
                result = result.multiply(BigInteger.valueOf(n - i));  // If i is less than or equal to k, multiply result by (n-i)
            } else {
                result = result.multiply(BigInteger.valueOf(n - k));  // If i is greater than k, multiply result by (n-k)
            }
        }

        // So far the result contains all the combinations where 1 or more songs are never played, therefore we need to
        // remove those combinations
        for (int j = 1; j < n - k; j++) {
            // j represents the number of songs that are never played.
            result = result.subtract(comb(n, j).multiply(numMusicPlaylistsHelper(n - j, goal, k)));  // Subtract the combinations where j songs are never played
        }

        memo[n][goal][k] = result.mod(M);  // Store the result in the memoization array
        return memo[n][goal][k];  // Return the result modulo M to prevent overflow
    }

    private BigInteger comb(int n, int k) {
        BigInteger result = BigInteger.ONE;
        for (int i = 0; i < k; i++) {
            result = result.multiply(BigInteger.valueOf(n - i)).divide(BigInteger.valueOf(i + 1));  // Calculate combination using the formula n! / (k!(n-k)!)
        }
        return result;
    }
}
