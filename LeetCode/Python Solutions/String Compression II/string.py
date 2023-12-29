class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # Initialize the memoization table
        memo = {}

        def dp(index, last_char, last_char_count, k):
            if k < 0:
                return float('inf')
            if index == len(s):
                return 0
            if (index, last_char, last_char_count, k) in memo:
                return memo[(index, last_char, last_char_count, k)]
            
            # Delete the current character
            delete = dp(index + 1, last_char, last_char_count, k - 1)
            
            # Keep the current character
            keep = float('inf')
            if s[index] == last_char:
                # Increase the count of the last character
                increase = 1 if last_char_count in [1, 9, 99] else 0
                keep = increase + dp(index + 1, last_char, min(last_char_count + 1, 100), k)
            else:
                # Start a new run with the current character
                keep = 1 + dp(index + 1, s[index], 1, k)
            
            # Memoize and return the minimum of keep and delete
            memo[(index, last_char, last_char_count, k)] = min(keep, delete)
            return memo[(index, last_char, last_char_count, k)]

        return dp(0, '', 0, k)
