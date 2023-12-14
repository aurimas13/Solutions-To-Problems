import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countNicePairs(int[] nums) {
        final int MOD = 1_000_000_007;
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            int key = num - rev(num);
            freq.put(key, freq.getOrDefault(key, 0) + 1);
        }

        long nicePairs = 0;
        for (int count : freq.values()) {
            nicePairs += (long) count * (count - 1) / 2;
            nicePairs %= MOD;
        }

        return (int) nicePairs;
    }

    private int rev(int x) {
        int reversed = 0;
        while (x > 0) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        return reversed;
    }
}
