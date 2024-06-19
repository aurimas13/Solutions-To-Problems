import java.util.Arrays;

class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        // Combine difficulty and profit into pairs and sort them by difficulty
        int[][] jobs = new int[difficulty.length][2];
        for (int i = 0; i < difficulty.length; i++) {
            jobs[i][0] = difficulty[i];
            jobs[i][1] = profit[i];
        }
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        
        // Sort workers by their abilities
        Arrays.sort(worker);
        
        int totalProfit = 0;
        int maxProfit = 0;
        int j = 0;
        
        for (int ability : worker) {
            while (j < jobs.length && jobs[j][0] <= ability) {
                maxProfit = Math.max(maxProfit, jobs[j][1]);
                j++;
            }
            totalProfit += maxProfit;
        }
        
        return totalProfit;
    }

    // Example usage:
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.maxProfitAssignment(new int[]{2, 4, 6, 8, 10}, new int[]{10, 20, 30, 40, 50}, new int[]{4, 5, 6, 7}));  // Output: 100
        System.out.println(s.maxProfitAssignment(new int[]{85, 47, 57}, new int[]{24, 66, 99}, new int[]{40, 25, 25}));  // Output: 0
    }
}