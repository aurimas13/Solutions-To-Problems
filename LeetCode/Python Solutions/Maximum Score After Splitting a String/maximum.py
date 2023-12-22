class Solution:
    def maxScore(self, s: str) -> int:
        # Count the total number of ones in the string.
        total_ones = s.count('1')
        
        # Initialize variables for the maximum score and the number of zeros and ones encountered so far.
        max_score, zeros, ones = 0, 0, 0
        
        # Iterate through the string, excluding the last character to ensure both substrings are non-empty.
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1  # Update the count of zeros in the left substring.
            else:
                ones += 1  # Update the count of ones in the left substring.
                
            # Calculate the score for the current split.
            score = zeros + (total_ones - ones)
            
            # Update the maximum score if the current score is higher.
            max_score = max(max_score, score)
        
        return max_score
