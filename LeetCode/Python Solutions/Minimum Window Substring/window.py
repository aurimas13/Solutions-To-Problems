from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = r = 0
        t_dict = Counter(t)
        window = {}
        ans = (float('inf'), None, None)
        required = len(t_dict)
        formed = 0

        while r < len(s):
            c = s[r]
            if c in t_dict:
                window[c] = window.get(c, 0) + 1
                if t_dict[c] == window[c]:
                    formed += 1

            while l <= r and formed == required:
                c = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                if c in t_dict:
                    window[c] -= 1
                    if window[c] < t_dict[c]:
                        formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minWindow("ADOBECODEBANC", "ABC")  # s = "ADOBECODEBANC", t = "ABC" -> "BANC" |  s = "a", t = "aa" -> ""
    print(Solve)
