class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Initialize the maximum length of the segment and the count of the maximum character in the current window
        max_length = max_count = 0
        
        # Initialize the left pointer of the sliding window
        left = 0
        count = {'T': 0, 'F': 0}
        
        # Loop through the answer key using the right pointer of the sliding window
        for right in range(len(answerKey)):
            # Update the count of the current character
            count[answerKey[right]] += 1
            
            # Keep track of the maximum count
            max_count = max(max_count, count[answerKey[right]])
            
            # If the window size minus maximum character frequency is greater than k, shrink the window
            if (right - left + 1) - max_count > k:
                # Decrease the count of the character that will be removed from the window
                count[answerKey[left]] -= 1
                # Move the left pointer to the right
                left += 1
            
            # Keep track of the maximum length of the segment
            max_length = max(max_length, right - left + 1)
        
        return max_length
