class Solution {
    public int longestPalindrome(String s) {
        int[] charCount = new int[128];
        
        // Count the frequency of each character
        for (char c : s.toCharArray()) {
            charCount[c]++;
        }
        
        int length = 0;
        boolean oddFound = false;
        
        // Iterate through the character counts
        for (int count : charCount) {
            if (count % 2 == 0) {
                // If the count is even, add it to the length
                length += count;
            } else {
                // If the count is odd, add count - 1 to the length
                length += count - 1;
                oddFound = true;
            }
        }
        
        // If there is any character with an odd count, we can add 1 to the length
        if (oddFound) {
            length++;
        }
        
        return length;
    }
}