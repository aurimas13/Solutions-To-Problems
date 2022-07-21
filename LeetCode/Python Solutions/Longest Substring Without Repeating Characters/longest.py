class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_length = 0

        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x) + 1:]

            str_list.append(x)
            max_length = max(max_length, len(str_list))

        return max_length


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.lengthOfLongestSubstring("abcabcbb")  # s = "abcabcbb" -> 3
    print(Solve)


# OR

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         ans = 0
#         # mp stores the current index of a character
#         mp = {}

#         i = 0
#         # try to extend the range [i, j]
#         for j in range(n):
#             if s[j] in mp:
#                 i = max(mp[s[j]], i)

#             ans = max(ans, j - i + 1)
#             mp[s[j]] = j + 1

#         return ans
