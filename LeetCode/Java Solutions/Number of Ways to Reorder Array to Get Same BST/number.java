import java.util.*;

class Solution {
    final int MOD = (int) (1e9 + 7);
    final int N = 1005;
    long[][] C = new long[N][N];

    public Solution() {
        // Pre-calculate combinations
        for(int i = 0; i < N; i++) {
            C[i][0] = C[i][i] = 1;
            for(int j = 1; j < i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }
    }

    public int numOfWays(int[] nums) {
        List<Integer> arr = new ArrayList<>();
        for(int num : nums) {
            arr.add(num);
        }
        return (int) (dfs(arr) - 1);
    }

    private long dfs(List<Integer> arr) {
        if(arr.size() == 0) {
            return 1;
        }
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for(int i = 1; i < arr.size(); i++) {
            if(arr.get(i) < arr.get(0)) {
                left.add(arr.get(i));
            } else {
                right.add(arr.get(i));
            }
        }
        return (((C[left.size() + right.size()][left.size()] * dfs(left)) % MOD) * dfs(right)) % MOD;
    }
}

