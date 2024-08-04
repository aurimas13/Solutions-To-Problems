import java.util.PriorityQueue;

class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        final int MOD = 1_000_000_007;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        
        // Initialize min-heap with [sum, index, end] for each number
        for (int i = 0; i < n; i++) {
            pq.offer(new int[]{nums[i], i, i});
        }
        
        int result = 0;
        for (int i = 1; i <= right; i++) {
            int[] curr = pq.poll();
            int currSum = curr[0], start = curr[1], end = curr[2];
            
            if (i >= left) {
                result = (result + currSum) % MOD;
            }
            
            if (end + 1 < n) {
                int nextSum = (int)(((long)currSum + nums[end + 1]) % MOD);
                pq.offer(new int[]{nextSum, start, end + 1});
            }
        }
        
        return result;
    }
}