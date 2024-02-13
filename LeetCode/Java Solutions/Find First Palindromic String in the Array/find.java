from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate through each word in the list
        for word in words:
            # Check if the word is a palindrome
            if word == word[::-1]:
                return word  # Return the first palindrome found
        return ""  # Return an empty string if no palindrome is found
