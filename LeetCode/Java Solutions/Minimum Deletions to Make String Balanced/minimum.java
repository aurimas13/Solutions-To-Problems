class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        
        # Step 1: Count the frequency of each character.
        char_freq = Counter(s)
        
        # Step 2: Create a set to keep track of the frequencies we have seen.
        freq_seen = set()
        
        deletions = 0
        for freq in char_freq.values():
            while freq in freq_seen:
                freq -= 1
                deletions += 1
            if freq > 0:
                freq_seen.add(freq)
        
        return deletions
