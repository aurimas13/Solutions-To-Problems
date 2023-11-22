import java.util.HashMap;
import java.util.PriorityQueue;

class Solution {
    public String reorganizeString(String s) {
        // Step 1: Count occurrences of each character
        HashMap<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) {
            counts.put(c, counts.getOrDefault(c, 0) + 1);
        }

        // Step 2: Create a max-heap
        PriorityQueue<Character> maxHeap = new PriorityQueue<>((a, b) -> counts.get(b) - counts.get(a));
        maxHeap.addAll(counts.keySet());

        // If most frequent character is more than half of string, then impossible to rearrange
        if (counts.get(maxHeap.peek()) > (s.length() + 1) / 2) {
            return "";
        }

        // Step 3: Arrange characters by placing the most frequent characters first
        char[] arr = new char[s.length()];
        int index = 0;

        while (!maxHeap.isEmpty()) {
            char current = maxHeap.poll();
            int times = counts.get(current);
            for (int i = 0; i < times; i++) {
                // If the even indexes are exhausted, start from the first odd index
                if (index >= arr.length) {
                    index = 1;
                }
                arr[index] = current;
                index += 2;
            }
        }

        return new String(arr);
    }
}
