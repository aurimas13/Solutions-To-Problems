class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        seen = {0: -1}
        state = max_len = 0
        
        for i, c in enumerate(s):
            if c in vowels:
                state ^= vowels[c]
            if state in seen:
                max_len = max(max_len, i - seen[state])
            else:
                seen[state] = i
        
        return max_len