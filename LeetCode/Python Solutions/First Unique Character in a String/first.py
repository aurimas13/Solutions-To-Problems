class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count the frequency of each character
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
            
        # Find the first character that appears only once
        for i, char in enumerate(s):
            if frequency[char] == 1:
                return i
        return -1

