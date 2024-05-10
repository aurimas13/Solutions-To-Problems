import java.util.PriorityQueue;

public class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.length;
        // Min-heap to store (fraction value, numerator index, denominator index)
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> {
            double fracA = (double) arr[a[0]] / arr[a[1]];
            double fracB = (double) arr[b[0]] / arr[b[1]];
            return Double.compare(fracA, fracB);
        });
        
        // Initial population of the heap
        for (int j = 1; j < n; j++) {
            minHeap.offer(new int[]{0, j});
        }
        
        // Extract the smallest fraction k-1 times
        for (int t = 0; t < k - 1; t++) {
            int[] fraction = minHeap.poll();
            int i = fraction[0], j = fraction[1];
            // Push the next fraction with the same denominator and the next numerator
            if (i + 1 < j) {
                minHeap.offer(new int[]{i + 1, j});
            }
        }
        
        return new int[]{arr[minHeap.peek()[0]], arr[minHeap.peek()[1]]};
    }
}
