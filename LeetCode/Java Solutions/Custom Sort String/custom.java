class Solution {
    public String customSortString(String order, String s) {
        // Count the frequency of each character in s
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        
        // Build the result string
        StringBuilder result = new StringBuilder();
        for (char c : order.toCharArray()) {
            while (freq[c - 'a'] > 0) {
                result.append(c);
                freq[c - 'a']--;
            }
        }
        
        // Append remaining characters not in order
        for (char c = 'a'; c <= 'z'; c++) {
            while (freq[c - 'a'] > 0) {
                result.append(c);
                freq[c - 'a']--;
            }
        }
        
        return result.toString();
    }
}
