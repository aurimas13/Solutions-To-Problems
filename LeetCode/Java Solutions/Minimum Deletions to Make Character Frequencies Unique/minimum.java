import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public int minDeletions(String s) {
        // Step 1: Count the frequency of each character.
        HashMap<Character, Integer> charFreq = new HashMap<>();
        for (char c : s.toCharArray()) {
            charFreq.put(c, charFreq.getOrDefault(c, 0) + 1);
        }
        
        // Step 2: Create a set to keep track of the frequencies we have seen.
        HashSet<Integer> freqSeen = new HashSet<>();
        
        int deletions = 0;
        for (int freq : charFreq.values()) {
            while (freqSeen.contains(freq)) {
                freq -= 1;
                deletions += 1;
            }
            if (freq > 0) {
                freqSeen.add(freq);
            }
        }
        
        return deletions;
    }
}
