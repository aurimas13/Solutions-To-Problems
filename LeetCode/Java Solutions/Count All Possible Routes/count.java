public class Solution {
    /**
     * Counts the number of possible routes from the start location to the finish location
     * given the fuel limit and locations of each point. Uses dynamic programming to
     * calculate the number of routes.
     *
     * @param  locations  an array of integers representing locations of each point
     * @param  start      an integer representing the starting location
     * @param  finish     an integer representing the finishing location
     * @param  fuel       an integer representing the fuel limit
     * @return            an integer representing the number of possible routes
     */

    public int countRoutes(int[] locations, int start, int finish, int fuel) {
        int mod = (int)1e9 + 7;
        int n = locations.length;
        long[][] dp = new long[fuel + 1][n];
        for (int f = 0; f <= fuel; f++) {
            dp[f][finish] = 1;
        }
        

        for (int f = fuel; f >= 0; f--) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (j == k) continue;
                    int d = Math.abs(locations[j] - locations[k]);
                    if (f + d <= fuel) {
                        dp[f][j] = (dp[f][j] + dp[f + d][k]) % mod;
                    }
                }
            }
        }
        return (int)dp[0][start];
    }
}