class Solution {
    public int firstUniqChar(String s) {
        // Store frequencies of each character
        int[] freq = new int[26]; // Assuming only lowercase English letters
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }
        
        // Find the first non-repeating character
        for (int i = 0; i < s.length(); i++) {
            if (freq[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}
