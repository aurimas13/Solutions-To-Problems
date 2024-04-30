import java.util.HashMap;
import java.util.Map;

class Solution {
    public long wonderfulSubstrings(String word) {
        // Map to store frequency of each bitmask
        Map<Integer, Long> maskCount = new HashMap<>();
        // Initialize with the empty prefix
        maskCount.put(0, 1L);
        
        long count = 0;
        int bitmask = 0;
        for (char c : word.toCharArray()) {
            // Flip the bit corresponding to the current character
            bitmask ^= (1 << (c - 'a'));
            
            // If this bitmask has been seen before, all those substrings are wonderful
            count += maskCount.getOrDefault(bitmask, 0L);
            
            // Check for substrings that have only one character with an odd count
            for (int i = 0; i < 10; i++) {
                int maskWithOneFlipped = bitmask ^ (1 << i);
                count += maskCount.getOrDefault(maskWithOneFlipped, 0L);
            }
            
            // Update the count of this bitmask in the map
            maskCount.put(bitmask, maskCount.getOrDefault(bitmask, 0L) + 1);
        }
        
        return count;
    }
}
