from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_dict = {}
        str1_dict = {}
        k = len(p)
        matches = 0
        result = []

        if k > len(s):
            return result

        for i in range(ord('a'), ord('z') + 1):
            pattern_dict[chr(i)] = 0
            str1_dict[chr(i)] = 0

        for i in range(k):
            pattern_dict[p[i]] += 1
            str1_dict[s[i]] += 1

        for i in range(ord('a'), ord('z') + 1):
            if pattern_dict[chr(i)] == str1_dict[chr(i)]:
                matches += 1

        if matches == 26:
            result.append(0)

        for window_end in range(k, len(s)):
            window_end_elem = s[window_end]
            str1_dict[window_end_elem] += 1
            if str1_dict[window_end_elem] == pattern_dict[window_end_elem]:
                matches += 1
            elif str1_dict[window_end_elem] - 1 == pattern_dict[window_end_elem]:
                matches -= 1

            window_start_elem = s[window_end - k]
            str1_dict[window_start_elem] -= 1
            if str1_dict[window_start_elem] == pattern_dict[window_start_elem]:
                matches += 1
            elif str1_dict[window_start_elem] + 1 == pattern_dict[window_start_elem]:
                matches -= 1

            if matches == 26:
                result.append(window_end - k + 1)

        return result


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findAnagrams(s = "cbaebabacd", p = "abc")  # s = "abab", p = "ab" -> [0,1,2] | s = "cbaebabacd", p = "abc" -> [0,6]
    print(Solve)
