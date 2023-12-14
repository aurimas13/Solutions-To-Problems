class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        // Initialize the maximum length of the segment and the count of the maximum character in the current window
        int max_length = 0, max_count = 0;
        
        // Initialize the left pointer of the sliding window
        int left = 0;
        int[] count = new int[2]; // count[0] for 'T', count[1] for 'F'
        
        // Loop through the answer key using the right pointer of the sliding window
        for (int right = 0; right < answerKey.length(); right++) {
            // Update the count of the current character
            count[answerKey.charAt(right) == 'T' ? 0 : 1]++;
            
            // Keep track of the maximum count
            max_count = Math.max(max_count, Math.max(count[0], count[1]));
            
            // If the window size minus maximum character frequency is greater than k, shrink the window
            if ((right - left + 1) - max_count > k) {
                // Decrease the count of the character that will be removed from the window
                count[answerKey.charAt(left) == 'T' ? 0 : 1]--;
                // Move the left pointer to the right
                left++;
            }
            
            // Keep track of the maximum length of the segment
            max_length = Math.max(max_length, right - left + 1);
        }
        
        return max_length;
    }
}
