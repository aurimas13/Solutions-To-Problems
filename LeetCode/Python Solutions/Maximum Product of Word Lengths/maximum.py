from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Create a list to store the bit representation of words
        bit_representation = []

        # Iterate through the words list
        for word in words:
            # Calculate the bit representation of the word
            bits = sum(1 << (ord(c) - ord('a')) for c in set(word))
            bit_representation.append(bits)

        # Initialize the maximum product to 0
        max_product = 0

        # Iterate through the bit_representation list
        for i in range(len(bit_representation)):
            for j in range(i + 1, len(bit_representation)):
                # Check if the words have no common letters by ANDing their bit representations
                if bit_representation[i] & bit_representation[j] == 0:
                    # Update the maximum product if the product of the word lengths is larger
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        # Return the maximum product
        return max_product


def run_tests():
    # Initialize the Solution class
    solution = Solution()

    # Test cases
    test_cases = [
        (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
        (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
        (["a", "aa", "aaa", "aaaa"], 0)
    ]

    # Run the test cases
    for i, (words, expected) in enumerate(test_cases):
        result = solution.maxProduct(words)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} succeeded")


if __name__ == "__main__":
    run_tests()



