import java.util.PriorityQueue;

class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        // Min heap to keep track of the largest jumps where ladders are used
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for (int i = 0; i < heights.length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            
            // If the next building is taller, add the difference to the heap
            if (diff > 0) {
                heap.add(diff);
            }
            
            // If we have more ladders than needed, remove the smallest jump from the heap
            if (heap.size() > ladders) {
                bricks -= heap.poll();
            }
            
            // If we run out of bricks, return the current index
            if (bricks < 0) {
                return i;
            }
        }
        
        // If we didn't run out of bricks, we can reach the last building
        return heights.length - 1;
    }
}
