class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0
        if not needle:
            return 0

        # If haystack is empty, return -1
        if not haystack:
            return -1

        # Iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack starting at index i matches the needle
            if haystack[i:i + len(needle)] == needle:
                return i

        # If the needle is not found in the haystack, return -1
        return -1

# Test cases
if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    haystack1 = "hello"
    needle1 = "ll"
    assert solution.strStr(haystack1, needle1) == 2

    # Test case 2
    haystack2 = "aaaaa"
    needle2 = "bba"
    assert solution.strStr(haystack2, needle2) == -1

    # Test case 3
    haystack3 = "abc"
    needle3 = ""
    assert solution.strStr(haystack3, needle3) == 0

    print("All test cases passed!")
