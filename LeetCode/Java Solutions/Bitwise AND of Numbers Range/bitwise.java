class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        // Shift right until left equals right
        while (left != right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        // Shift left back to its original position with zeroes appended
        return left << shift;
    }
}
