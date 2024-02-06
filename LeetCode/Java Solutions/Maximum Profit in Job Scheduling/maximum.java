import java.util.Arrays;
import java.util.TreeMap;

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][3];
        for (int i = 0; i < n; i++) {
            jobs[i] = new int[]{startTime[i], endTime[i], profit[i]};
        }
        Arrays.sort(jobs, (a, b) -> a[1] - b[1]);
        
        // TreeMap to store the max profit up to the current time
        TreeMap<Integer, Integer> dp = new TreeMap<>();
        dp.put(0, 0); // Initial value

        for (int[] job : jobs) {
            int curProfit = dp.floorEntry(job[0]).getValue() + job[2];
            if (curProfit > dp.lastEntry().getValue()) {
                dp.put(job[1], curProfit);
            }
        }
        
        return dp.lastEntry().getValue();
    }
}
