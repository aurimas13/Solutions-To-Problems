import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int countCharacters(String[] words, String chars) {
        // Map to store the count of each character in chars
        Map<Character, Integer> charsCount = new HashMap<>();
        for (char c : chars.toCharArray()) {
            charsCount.put(c, charsCount.getOrDefault(c, 0) + 1);
        }

        int totalLength = 0;

        for (String word : words) {
            Map<Character, Integer> wordCount = new HashMap<>();
            for (char c : word.toCharArray()) {
                wordCount.put(c, wordCount.getOrDefault(c, 0) + 1);
            }

            // Check if the word can be formed by chars
            boolean canForm = true;
            for (char c : word.toCharArray()) {
                if (!charsCount.containsKey(c) || wordCount.get(c) > charsCount.get(c)) {
                    canForm = false;
                    break;
                }
            }

            if (canForm) {
                totalLength += word.length();
            }
        }

        return totalLength;
    }
}
