class Solution {
    public int minTaps(int n, int[] ranges) {
        int[] maxRange = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int left = Math.max(0, i - ranges[i]);
            int right = Math.min(n, i + ranges[i]);
            maxRange[left] = Math.max(maxRange[left], right);
        }
        
        // Greedy approach
        int start = 0, end = 0, taps = 0;
        while (end < n) {
            int newEnd = end;
            for (int i = start; i <= end; i++) {
                newEnd = Math.max(newEnd, maxRange[i]);
            }
            if (newEnd == end) {
                return -1;
            }
            start = end;
            end = newEnd;
            taps++;
        }
        return taps;
    }
}
