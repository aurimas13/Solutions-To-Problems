class Solution {
    public int maxScore(String s) {
        // Count the total number of ones in the string.
        int totalOnes = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') totalOnes++;
        }
        
        // Initialize variables for the maximum score and the number of zeros and ones encountered so far.
        int maxScore = 0, zeros = 0, ones = 0;
        
        // Iterate through the string, excluding the last character to ensure both substrings are non-empty.
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '0') {
                zeros++;  // Update the count of zeros in the left substring.
            } else {
                ones++;  // Update the count of ones in the left substring.
            }
            
            // Calculate the score for the current split.
            int score = zeros + (totalOnes - ones);
            
            // Update the maximum score if the current score is higher.
            maxScore = Math.max(maxScore, score);
        }
        
        return maxScore;
    }
}
