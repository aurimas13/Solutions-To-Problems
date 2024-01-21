import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean makeEqual(String[] words) {
        Map<Character, Integer> charCount = new HashMap<>();

        // Count all characters in all words
        for (String word : words) {
            for (char c : word.toCharArray()) {
                charCount.put(c, charCount.getOrDefault(c, 0) + 1);
            }
        }

        // Check if each character's total count is divisible by the number of words
        for (int count : charCount.values()) {
            if (count % words.length != 0) {
                return false;
            }
        }

        return true;
    }
}
