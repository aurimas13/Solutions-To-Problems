class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Create a set to store unique substrings
        unique_substrings = set()

        def backtrack(start):
            # Base case: all substrings have been processed
            if start == len(s):
                return 0

            # Initialize the maximum number of unique substrings
            max_count = 0

            # Try all possible substrings starting from the current position
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                # If the substring has not been seen before, add it to the set
                if substring not in unique_substrings:
                    unique_substrings.add(substring)

                    # Recursively process the remaining part of the string
                    count = backtrack(end)

                    # Update the maximum count
                    max_count = max(max_count, count + 1)

                    # Remove the substring from the set for backtracking
                    unique_substrings.remove(substring)

            return max_count

        # Call the backtrack function starting from the first character
        return backtrack(0)


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maxUniqueSplit(s = "ababccc") 
    # s = "ababccc" -> 5
    # s = "aba" -> 2
    # s = "aa" -> 1
    print(Solve)

