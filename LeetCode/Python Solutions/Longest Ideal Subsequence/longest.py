class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # dp[c] will hold the maximum length of the ideal subsequence ending with character c
        dp = [0] * 128  # ASCII size suffices since we're only dealing with lowercase letters
        
        # Process each character in the string s
        for char in s:
            # Get ASCII value of the character for direct dp indexing
            idx = ord(char)
            
            # Calculate the maximum length of an ideal subsequence ending with `char`
            max_len = 0
            # Look at all characters within the distance `k` in the alphabet
            for i in range(max(97, idx - k), min(122, idx + k) + 1):  # 'a' to 'z' bounds
                max_len = max(max_len, dp[i])
            
            # Update the dp value for the current character
            dp[idx] = max_len + 1
        
        # The answer is the maximum value in dp for all characters 'a' to 'z'
        return max(dp[97:123])  # From ASCII of 'a' to 'z'
