from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        freq = Counter(s)
        
        # Sort characters by frequency and lexicographical order as tie breaker
        chars_sorted_by_freq = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        
        # Build the result string
        result = ''.join(char * freq[char] for char in chars_sorted_by_freq)
        
        return result
