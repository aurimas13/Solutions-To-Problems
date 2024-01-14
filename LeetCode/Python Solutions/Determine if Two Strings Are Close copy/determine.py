class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if the lengths of the strings are the same
        if len(word1) != len(word2):
            return False
        
        # Count the frequency of characters in both strings
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        for c in word1:
            freq1[ord(c) - ord('a')] += 1
        
        for c in word2:
            freq2[ord(c) - ord('a')] += 1
        
        # Check if the sets of characters are the same
        if set(word1) != set(word2):
            return False
        
        # Check if the frequency of characters is the same (ignoring the order)
        return sorted(freq1) == sorted(freq2)

