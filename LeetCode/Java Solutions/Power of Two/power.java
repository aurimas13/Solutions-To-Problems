class Solution {
    public boolean isPowerOfTwo(int n) {
        // A number is a power of two if it is greater than 0 and the bitwise AND of n and n-1 is 0
        return n > 0 && (n & (n - 1)) == 0;
    }
}
