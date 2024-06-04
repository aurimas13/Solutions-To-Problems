class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        
        # Count the frequency of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        length = 0
        odd_found = False
        
        # Iterate through the character counts
        for count in char_count.values():
            if count % 2 == 0:
                # If the count is even, add it to the length
                length += count
            else:
                # If the count is odd, add count - 1 to the length
                length += count - 1
                odd_found = True
        
        # If there is any character with an odd count, we can add 1 to the length
        if odd_found:
            length += 1
        
        return length