class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Define a set of vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Calculate the initial count of vowels in the first window of length k
        initial_vowel_count = sum([1 for c in s[:k] if c in vowels])

        # Initialize the maximum vowel count to the initial vowel count
        max_vowel_count = initial_vowel_count

        # Iterate through the string with a sliding window of length k
        for i in range(k, len(s)):
            # Check if the character being removed is a vowel and decrease the count accordingly
            initial_vowel_count -= s[i - k] in vowels

            # Check if the character being added is a vowel and increase the count accordingly
            initial_vowel_count += s[i] in vowels

            # Update the maximum vowel count
            max_vowel_count = max(max_vowel_count, initial_vowel_count)

        return max_vowel_count

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxVowels("abciiidef", 3) == 3
    assert solution.maxVowels("aeiou", 2) == 2
    assert solution.maxVowels("leetcode", 3) == 2
    assert solution.maxVowels("rhythms", 4) == 0
    print("All tests passed.")
