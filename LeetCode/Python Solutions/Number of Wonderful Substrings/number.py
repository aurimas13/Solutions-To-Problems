class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Dictionary to store frequency of each bitmask
        mask_count = {0: 1}  # Initialize with the empty prefix
        result = 0
        bitmask = 0
        
        for char in word:
            # Calculate bitmask for the current character
            bitmask ^= (1 << (ord(char) - ord('a')))
            
            # If this bitmask has been seen before, add those substrings to the result
            result += mask_count.get(bitmask, 0)
            
            # Check for substrings that have only one character with an odd count
            for i in range(10):  # Since 'a' to 'j' are 10 letters
                # Create a new mask with one bit flipped
                mask_with_one_flipped = bitmask ^ (1 << i)
                result += mask_count.get(mask_with_one_flipped, 0)
            
            # Update the count of this bitmask in the map
            mask_count[bitmask] = mask_count.get(bitmask, 0) + 1
        
        return result
