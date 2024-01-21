class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(st):
            vowels = set("aeiouAEIOU")
            return sum(char in vowels for char in st)

        mid = len(s) // 2
        return count_vowels(s[:mid]) == count_vowels(s[mid:])
