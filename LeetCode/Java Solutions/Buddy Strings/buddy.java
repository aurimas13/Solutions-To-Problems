class Solution {
    public boolean buddyStrings(String s, String goal) {
        // If lengths of strings are different, they can't be equal
        if (s.length() != goal.length()) {
            return false;
        }
        
        // If strings are already equal
        if (s.equals(goal)) {
            int[] count = new int[26];
            
            // Count the occurrences of each character
            for (int i = 0; i < s.length(); i++) {
                count[s.charAt(i) - 'a']++;
            }
            
            // Check if any character is repeated
            for (int c: count) {
                if (c > 1) {
                    return true;
                }
            }
            return false;
        }
        
        // Otherwise, find the indices of characters which are different
        int first = -1, second = -1, count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != goal.charAt(i)) {
                count++;
                if (first == -1) {
                    first = i;
                } else {
                    second = i;
                }
            }
        }
        
        // If there are exactly two indices (i, j) such that
        // s.charAt(i) == goal.charAt(j) and s.charAt(j) == goal.charAt(i), return True
        return count == 2 && s.charAt(first) == goal.charAt(second) && s.charAt(second) == goal.charAt(first);
    }
}
