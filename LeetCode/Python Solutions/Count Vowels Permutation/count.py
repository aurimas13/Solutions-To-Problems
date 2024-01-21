class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # Define the modulo constant
        MOD = 1000000007

        # Define the rules for vowel permutations
        rules = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        # Initialize the memoization dictionary
        memo = {}

        # Define the recursive function for counting vowel permutations
        def count_permutations(vowel, n):
            # Base case: when n is 1, there's only one permutation (the vowel itself)
            if n == 1:
                return 1

            # Check if the result is already in the memoization dictionary
            if (vowel, n) in memo:
                return memo[(vowel, n)]

            # Calculate the permutations using the rules and recursion
            total = sum(count_permutations(next_vowel, n - 1) for next_vowel in rules[vowel]) % MOD

            # Store the result in the memoization dictionary
            memo[(vowel, n)] = total

            return total

        # Calculate the total number of permutations for each vowel
        result = sum(count_permutations(vowel, n) for vowel in rules) % MOD

        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.countVowelPermutation(1) == 5
    assert solution.countVowelPermutation(2) == 10
    assert solution.countVowelPermutation(5) == 68
