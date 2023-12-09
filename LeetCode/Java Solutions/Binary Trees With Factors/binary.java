import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        long MOD = (long)1e9 + 7;

        // Sort the array
        Arrays.sort(arr);

        // This hashmap holds the number of trees with 'key' as root.
        HashMap<Integer, Long> dp = new HashMap<>();
        for (int num : arr) {
            dp.put(num, 1L); // A single node is a valid tree.
        }

        // For each number, we check if it can be the root of a new tree.
        for (int i = 0; i < arr.length; ++i) {
            for (int j = 0; j < i; ++j) {
                // If the number can be obtained by multiplying two numbers in the array
                if (arr[i] % arr[j] == 0) {
                    int right = arr[i] / arr[j];
                    // If both parts are in the hashmap, it's a valid combination.
                    if (dp.containsKey(right)) {
                        dp.put(arr[i], (dp.get(arr[i]) + dp.get(arr[j]) * dp.get(right)) % MOD);
                    }
                }
            }
        }

        long result = 0;
        for (long x : dp.values()) {
            result = (result + x) % MOD;
        }
        return (int)result;
    }
}
