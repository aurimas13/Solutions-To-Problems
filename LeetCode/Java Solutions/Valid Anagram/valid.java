public class Solution {
    public boolean isAnagram(String s, String t) {
        // An anagram must have the same length
        if (s.length() != t.length()) {
            return false;
        }

        // Count the frequency of each character in both strings
        int[] count = new int[26]; // Assuming only lowercase English letters

        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        // Check if all counts are zero
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }

        return true;
    }
}
