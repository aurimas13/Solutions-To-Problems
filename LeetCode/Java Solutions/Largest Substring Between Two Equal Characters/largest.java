class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int[] firstOccurrence = new int[26];  // Array to store the first occurrence index of each character
        java.util.Arrays.fill(firstOccurrence, -1);  // Initialize with -1
        int maxLength = -1;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // If the character has appeared before, calculate the length
            if (firstOccurrence[c - 'a'] != -1) {
                maxLength = Math.max(maxLength, i - firstOccurrence[c - 'a'] - 1);
            } else {
                // Store the first occurrence of the character
                firstOccurrence[c - 'a'] = i;
            }
        }

        return maxLength;
    }
}

