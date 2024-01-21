import re
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if str(num).count('0') > 1 or str(num).count('0') == 0:
            return str(num) == str(num)[::-1].strip('0')[::-1]
        elif str(num).count('0') == 1:
            if str(num) == '0':
                return True
            else:
                return str(num) == str(num)[::-1].strip('0')[::-1]

if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.isSameAfterReversals(536)  # for 1800 - false, for 0 - true, for 536 - true, 10 - false
    print(Solve)