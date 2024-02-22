class Solution {
    public int findJudge(int n, int[][] trust) {
        if (trust.length < n - 1) {
            return -1;  // A judge can't exist if there are less trust relationships than n-1
        }

        // Initialize trust counts
        int[] trustCounts = new int[n + 1];

        // Calculate trust counts
        for (int[] relation : trust) {
            trustCounts[relation[0]]--;  // Person a trusts someone, decrease their count
            trustCounts[relation[1]]++;  // Person b is trusted by someone, increase their count
        }

        // Find the town judge
        for (int i = 1; i <= n; i++) {
            if (trustCounts[i] == n - 1) {
                return i;  // The judge is found
            }
        }

        return -1;  // No judge found
    }
}


