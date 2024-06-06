import java.util.*;

class Solution {
    public List<String> commonChars(String[] words) {
        List<String> result = new ArrayList<>();
        if (words == null || words.length == 0) return result;

        // Initialize the common count with the first word's character count
        int[] commonCount = new int[26];
        for (char c : words[0].toCharArray()) {
            commonCount[c - 'a']++;
        }

        // Intersect the counts with the remaining words
        for (int i = 1; i < words.length; i++) {
            int[] wordCount = new int[26];
            for (char c : words[i].toCharArray()) {
                wordCount[c - 'a']++;
            }
            for (int j = 0; j < 26; j++) {
                commonCount[j] = Math.min(commonCount[j], wordCount[j]);
            }
        }

        // Build the result list based on the final common counts
        for (int i = 0; i < 26; i++) {
            while (commonCount[i] > 0) {
                result.add(String.valueOf((char)(i + 'a')));
                commonCount[i]--;
            }
        }

        return result;
    }

    // Example usage
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.commonChars(new String[]{"bella", "label", "roller"}));  // Output: ["e","l","l"]
        System.out.println(sol.commonChars(new String[]{"cool", "lock", "cook"}));  // Output: ["c","o"]
    }
}
