class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        while index < n and s[index] == ' ':
            index += 1
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1
        while index < n and s[index].isdigit():
            digit = int(s[index])
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            index += 1
        return sign * result

# Checking in PyCharm console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.myAtoi("+1")  # "42" -> 42 | "-42" -> -42 | "words with 971" -> 0 | "   564" -> 564 | "-91283472332" -> -2147483647 | "3.1423 -> 3 | '+1' -> 1
    print(Solve)


# all_str = list(map(str, s.split()))
# # for i in range(len(all_str)):
# print(all_str)
# if len(all_str) > 0:
#     if all_str[0].replace('.','').isdigit() or all_str[0].lstrip('-').replace('.','').isdigit() or all_str[0].lstrip('+').replace('.','').isdigit():
#         number = all_str[0].lstrip()
#         number = number if isinstance(number, int) else float(number)
#         if -2147483647 < number < 2147483647 or -2147483647 < number < 2147483647:
#             return int(number)
#         elif int(all_str[0]) < -2147483647 or float(all_str[0]) < -2147483647:
#             return -2147483648
#         elif int(all_str[0]) > 2147483647 or float(all_str[0]) < -2147483647:
#             return 2147483647
#     else:
#         return 0
# else:
#     return 0
