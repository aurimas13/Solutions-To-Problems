class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}  # Stores the first occurrence index of each character
        max_length = -1

        for i, char in enumerate(s):
            if char in first_occurrence:
                # Calculate the length between the first and current occurrence of the character
                max_length = max(max_length, i - first_occurrence[char] - 1)
            else:
                # Store the first occurrence of the character
                first_occurrence[char] = i

        return max_length

