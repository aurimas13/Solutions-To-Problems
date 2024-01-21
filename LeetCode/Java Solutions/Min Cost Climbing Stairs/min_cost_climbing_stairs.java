public class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return cost[0];
        }
        
        int[] minCost = new int[n];
        minCost[0] = cost[0];
        minCost[1] = cost[1];
        
        for (int i = 2; i < n; i++) {
            minCost[i] = cost[i] + Math.min(minCost[i-1], minCost[i-2]);
        }
        
        return Math.min(minCost[n-1], minCost[n-2]);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        
        // Test cases
        System.out.println(s.minCostClimbingStairs(new int[]{10, 15, 20}));  // 15
        System.out.println(s.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}));  // 6
    }
}

