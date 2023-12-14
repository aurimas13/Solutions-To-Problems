class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        for char in set(s):  # Iterate over each unique character
            first = s.find(char)  # Find the first occurrence
            last = s.rfind(char)  # Find the last occurrence
            if first != last:  # Ensure there are characters in between
                count += len(set(s[first+1:last]))  # Count unique characters in between
        return count
