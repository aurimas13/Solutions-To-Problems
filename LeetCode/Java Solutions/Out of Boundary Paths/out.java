import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final int MOD = 1000000007;
    private Map<String, Integer> memo = new HashMap<>();

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        return dp(m, n, maxMove, startRow, startColumn);
    }

    private int dp(int m, int n, int move, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n) return 1;
        if (move == 0) return 0;
        String key = move + "," + i + "," + j;
        if (memo.containsKey(key)) return memo.get(key);

        int paths = (int) (((long) dp(m, n, move - 1, i + 1, j) + dp(m, n, move - 1, i - 1, j) +
                dp(m, n, move - 1, i, j + 1) + dp(m, n, move - 1, i, j - 1)) % MOD);

        memo.put(key, paths);
        return paths;
    }
}
