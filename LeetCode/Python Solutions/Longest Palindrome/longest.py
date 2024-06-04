class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Initialize the length of the string
        n = len(s)
        
        # Create a 2D list to store the lengths of the longest palindromic subsequences
        dp = [[0] * n for _ in range(n)]
        
        # Set the diagonal elements to 1, since single characters are always palindromic
        for i in range(n):
            dp[i][i] = 1
        
        # Iterate through the string in reverse order
        for i in range(n - 1, -1, -1):
            # Iterate through the string starting from i + 1
            for j in range(i + 1, n):
                # If the characters at positions i and j are equal
                if s[i] == s[j]:
                    # Increment the length of the longest palindromic subsequence
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # If the characters at positions i and j are not equal
                else:
                    # Update the longest palindromic subsequence length
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # Return the length of the longest palindromic subsequence
        return dp[0][n - 1]

if __name__ == '__main__':
    s = Solution()
    
    # Test cases
    test1 = "bbbab"
    test2 = "cbbd"
    test3 = "abcdefg"

    print(f"Longest Palindromic Subsequence for '{test1}' is: {s.longestPalindromeSubseq(test1)}")  # Expected: 4
    print(f"Longest Palindromic Subsequence for '{test2}' is: {s.longestPalindromeSubseq(test2)}")  # Expected: 2
    print(f"Longest Palindromic Subsequence for '{test3}' is: {s.longestPalindromeSubseq(test3)}")  # Expected: 1
