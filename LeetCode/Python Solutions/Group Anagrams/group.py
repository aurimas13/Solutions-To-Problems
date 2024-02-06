from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Using defaultdict to automatically handle missing keys
        
        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort the characters of the word
            anagrams[sorted_word].append(word)  # Group by sorted_word
        
        return list(anagrams.values())  # Return grouped anagrams
