# class Solution:
#     def romanToInt(self, s: str) -> int:
#             rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#             int_val = 0
#             for i in range(len(s)):
#                 if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
#                     int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
#                 else:
#                     int_val += rom_val[s[i]]
#             return int_val
#

# or

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.romanToInt("MCMXCIV")  #  "MCMXCIV" -> 1994; "LVIII" -> 58
    print(Solve)