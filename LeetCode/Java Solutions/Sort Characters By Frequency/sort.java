import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        
        // Count the frequency of each character
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        
        // Use a priority queue to sort characters by their frequency
        PriorityQueue<Character> maxHeap = new PriorityQueue<>((a, b) -> freq.get(b) - freq.get(a));
        maxHeap.addAll(freq.keySet());
        
        // Build the result string
        StringBuilder result = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            char c = maxHeap.remove();
            for (int i = 0; i < freq.get(c); i++) {
                result.append(c);
            }
        }
        
        return result.toString();
    }
}
