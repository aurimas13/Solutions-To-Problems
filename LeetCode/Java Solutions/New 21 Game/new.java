class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if (k == 0 || n >= k + maxPts)
            return 1.0;

        double[] dp = new double[n + 1];
        dp[0] = 1.0;
        double sum = 1.0;
        double result = 0.0;

        for (int i = 1; i <= n; i++) {
            dp[i] = sum / maxPts;
            if (i < k)
                sum += dp[i];
            else
                result += dp[i];
            if (i - maxPts >= 0)
                sum -= dp[i - maxPts];
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.new21Game(10, 1, 10));  // 1.0
        System.out.println(solution.new21Game(6, 1, 10));  // 0.6
        System.out.println(solution.new21Game(21, 17, 10));  // 0.7327777870686075
        System.out.println(solution.new21Game(1, 0, 1));  // 1.0
    }
}
