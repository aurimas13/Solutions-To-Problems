class Solution {
    public int passThePillow(int n, int time) {
        int cycleLength = 2 * (n - 1);
        int effectiveTime = time % cycleLength;

        if (effectiveTime < n) {
            return effectiveTime + 1;
        } else {
            return 2 * n - 1 - effectiveTime;
        }
    }
}
