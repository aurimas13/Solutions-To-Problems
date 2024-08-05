import java.util.HashMap;
import java.util.Map;

class Solution {
    public String kthDistinct(String[] arr, int k) {
        // Count occurrences of each string
        Map<String, Integer> count = new HashMap<>();
        for (String s : arr) {
            count.put(s, count.getOrDefault(s, 0) + 1);
        }
        
        // Find the kth distinct string
        int distinctCount = 0;
        for (String s : arr) {
            if (count.get(s) == 1) {
                distinctCount++;
                if (distinctCount == k) {
                    return s;
                }
            }
        }
        
        // If there are fewer than k distinct strings, return ""
        return "";
    }
}