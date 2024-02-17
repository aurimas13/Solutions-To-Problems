import java.util.*;

class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        // Count the frequency of each integer
        for (int num : arr) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        // Min heap to store integers by their frequency
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Comparator.comparing(freq::get));
        minHeap.addAll(freq.keySet());
        
        // Remove least frequent integers first
        while (k > 0 && !minHeap.isEmpty()) {
            int current = minHeap.poll();
            int currentFreq = freq.get(current);
            if (k >= currentFreq) {
                k -= currentFreq;  // Use k removals for this integer
            } else {
                // If k is not enough to remove all instances of the current integer, stop
                freq.put(current, currentFreq - k);
                k = 0;
                minHeap.add(current);  // Re-add the current with its remaining count
            }
        }
        
        // Number of unique integers left
        return minHeap.size();
    }
}
