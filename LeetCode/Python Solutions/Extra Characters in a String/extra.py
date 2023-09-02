class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Initialize the maximum possible value for dp
        max_val = len(s) + 1
        
        # Create a dp array initialized with max_val
        dp = [max_val] * (len(s) + 1)
        
        # Base case: 0 characters from s have 0 extra characters
        dp[0] = 0 
        
        # Convert the dictionary list to a set for O(1) lookups
        dictionary_set = set(dictionary)

        # Iterate through the string s
        for i in range(1, len(s) + 1):
            # By default, assume we add an extra character for position i
            dp[i] = dp[i - 1] + 1

            # Check all possible lengths of words ending at position i
            for l in range(1, i + 1): 
                # If the substring is in the dictionary
                if s[i-l:i] in dictionary_set:
                    # Update the dp value for position i
                    dp[i] = min(dp[i], dp[i-l])
                    
        # Return the dp value for the entire string
        return dp[-1]
