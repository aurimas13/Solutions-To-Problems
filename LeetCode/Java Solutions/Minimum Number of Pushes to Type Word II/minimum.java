import java.util.*;

class Solution {
    public int minimumPushes(String word) {
        // Count frequency of each letter
        int[] freq = new int[26];
        for (char c : word.toCharArray()) {
            freq[c - 'a']++;
        }
        
        // Sort frequencies in descending order
        Integer[] sortedFreq = new Integer[26];
        for (int i = 0; i < 26; i++) {
            sortedFreq[i] = freq[i];
        }
        Arrays.sort(sortedFreq, Collections.reverseOrder());
        
        int totalPushes = 0;
        for (int i = 0; i < 26; i++) {
            // Calculate number of pushes for this letter
            int pushes = (i / 8 + 1) * sortedFreq[i];
            totalPushes += pushes;
        }
        
        return totalPushes;
    }
}