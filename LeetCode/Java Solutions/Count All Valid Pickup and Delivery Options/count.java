class Solution {
    private static final int MOD = 1000000007;
    
    public int countOrders(int n) {
        long res = 1;
        
        // Calculate the result using the formula
        for (int i = 1; i <= n; i++) {
            res = (res * i * (2 * i - 1)) % MOD;
        }
        
        return (int) res;
    }
}
