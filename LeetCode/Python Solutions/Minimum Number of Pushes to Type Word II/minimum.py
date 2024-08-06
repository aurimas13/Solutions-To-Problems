from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter
        freq = Counter(word)
        
        # Sort letters by frequency, most frequent first
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_freq):
            # Calculate number of pushes for this letter
            pushes = (i // 8 + 1) * count
            total_pushes += pushes
        
        return total_pushes