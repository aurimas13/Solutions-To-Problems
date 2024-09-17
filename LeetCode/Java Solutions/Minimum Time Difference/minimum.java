class Solution {
    public int findMinDifference(List<String> timePoints) {
        if (timePoints.size() > 1440) return 0; // Pigeonhole principle

        boolean[] seen = new boolean[1440]; // 24 * 60 minutes in a day
        for (String time : timePoints) {
            int minutes = toMinutes(time);
            if (seen[minutes]) return 0; // Duplicate time
            seen[minutes] = true;
        }

        int first = Integer.MAX_VALUE, last = Integer.MIN_VALUE;
        int prev = -1, minDiff = Integer.MAX_VALUE;

        for (int i = 0; i < 1440; i++) {
            if (seen[i]) {
                if (prev != -1) {
                    minDiff = Math.min(minDiff, i - prev);
                }
                first = Math.min(first, i);
                last = Math.max(last, i);
                prev = i;
            }
        }

        // Check the difference between the last and first time points
        minDiff = Math.min(minDiff, 1440 - last + first);

        return minDiff;
    }

    private int toMinutes(String time) {
        String[] parts = time.split(":");
        return Integer.parseInt(parts[0]) * 60 + Integer.parseInt(parts[1]);
    }
}