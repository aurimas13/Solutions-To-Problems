class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if len(s) <= 1:
            return s
        start = end = 0
        length = len(s)
        for i in range(length):
            max_len_1 = self.get_max_len(s, i, i + 1)
            max_len_2 = self.get_max_len(s, i, i)
            max_len = max(max_len_1, max_len_2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end + 1]

    def get_max_len(self, s: 'list', left: 'int', right: 'int') -> 'int':
        length = len(s)
        i = 1
        max_len = 0
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


# Tests:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestPalindrome("babad")  # "babad" -> "bab" | "cbbd" -> "bb"
    print(Solve)

# # Time Limit Exceeded for solution:
# m = ''  # Memory to remember a palindrome
# for i in range(len(s)):  # i = start, O = n
#     for j in range(len(s), i, -1):  # j = end, O = n^2
#         if len(m) >= j-i:  # To reduce time
#             break
#         elif s[i:j] == s[i:j][::-1]:
#             m = s[i:j]
#             break
# return m