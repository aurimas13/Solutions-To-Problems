import java.util.PriorityQueue;

class Solution {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        
        // Add all elements to the max heap
        for (int num : nums) {
            maxHeap.offer(num);
        }
        
        long score = 0;
        
        // Perform k operations
        for (int i = 0; i < k; i++) {
            int max = maxHeap.poll();
            score += max;
            maxHeap.offer((max + 2) / 3); // Equivalent to ceil(max / 3)
        }
        
        return score;
    }
}