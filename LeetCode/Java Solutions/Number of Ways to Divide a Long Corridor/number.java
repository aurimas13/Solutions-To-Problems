public class Solution {
    public int numberOfWays(String corridor) {
        final int MOD = 1_000_000_007;

        int seatCount = 0;
        // Count the total number of seats
        for (int i = 0; i < corridor.length(); i++) {
            if (corridor.charAt(i) == 'S') {
                seatCount++;
            }
        }

        // If not divisible by 2 or zero, return 0
        if (seatCount % 2 != 0 || seatCount == 0) {
            return 0;
        }

        long ways = 1;
        int seatPairs = 0, plantCount = 0;

        for (int i = 0; i < corridor.length(); i++) {
            if (corridor.charAt(i) == 'S') {
                seatPairs++;
                if (seatPairs % 2 == 0 && seatPairs > 2) {
                    // For every valid pair of seats after the first two seats, multiply the ways
                    ways = (ways * (plantCount + 1)) % MOD;
                    plantCount = 0;
                } else if (seatPairs % 2 == 0) {
                    plantCount = 0;
                }
            } else if (seatPairs % 2 == 0 && seatPairs >= 2) {
                // Count plants between pairs of seats
                plantCount++;
            }
        }

        return (int) ways;
    }
}
