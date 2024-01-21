from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialize dictionaries for pattern and string
        pattern_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        str1_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        k = len(p)  # Length of the pattern
        matches = 0  # Number of matched characters
        result = []  # Result list to store the starting indices of anagrams

        # If the pattern length is greater than the string length, return empty list
        if k > len(s):
            return result

        # Count the occurrences of characters in pattern and first k characters in string
        for i in range(k):
            pattern_dict[p[i]] += 1
            str1_dict[s[i]] += 1

        # Count matches between pattern_dict and str1_dict
        matches = sum(pattern_dict[chr(i)] == str1_dict[chr(i)] for i in range(ord('a'), ord('z') + 1))

        # If all characters match, append the starting index to the result list
        if matches == 26:
            result.append(0)

        # Iterate through the string, updating str1_dict and checking for anagrams
        for window_end in range(k, len(s)):
            window_end_elem = s[window_end]
            str1_dict[window_end_elem] += 1

            # Check if the current window_end_elem is matching the pattern
            if str1_dict[window_end_elem] == pattern_dict[window_end_elem]:
                matches += 1
            elif str1_dict[window_end_elem] - 1 == pattern_dict[window_end_elem]:
                matches -= 1

            window_start_elem = s[window_end - k]
            str1_dict[window_start_elem] -= 1

            # Check if the current window_start_elem is matching the pattern
            if str1_dict[window_start_elem] == pattern_dict[window_start_elem]:
                matches += 1
            elif str1_dict[window_start_elem] + 1 == pattern_dict[window_start_elem]:
                matches -= 1

            # If all characters match, append the starting index to the result list
            if matches == 26:
                result.append(window_end - k + 1)

        return result


# Running in terminal/console:
if __name__ == '__main__':
    instance = Solution()
    result = instance.findAnagrams(s="cbaebabacd", p="abc")  # s = "abab", p = "ab" -> [0,1,2] | s = "cbaebabacd", p = "abc" -> [0,6]
    print(result)
