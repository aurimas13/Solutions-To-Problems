class Solution {
    public int minimumOneBitOperations(int n) {
        int result = 0;
        while (n > 0) {
            result ^= n;
            n >>= 1;
        }
        return result;
    }
}
