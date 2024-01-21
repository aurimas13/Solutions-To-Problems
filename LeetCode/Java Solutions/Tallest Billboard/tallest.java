import java.util.*;

class Solution {
    /**
     * Calculates the maximum height possible for a billboard using the given array of rod heights.
     *
     * @param  rods  an array of integers representing the heights of the rods
     * @return       the maximum height possible for the billboard
     */
    public int tallestBillboard(int[] rods) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 0);
        for (int x : rods) {
            Map<Integer, Integer> dp2 = new HashMap<>(dp);
            for (int d : dp.keySet()) {
                dp2.put(d + x, Math.max(dp2.getOrDefault(d + x, 0), dp.get(d)));
                dp2.put(Math.abs(d - x), Math.max(dp2.getOrDefault(Math.abs(d - x), 0), dp.get(d) + Math.min(d, x)));
            }
            dp = dp2;
        }
        return dp.get(0);
    }
}
