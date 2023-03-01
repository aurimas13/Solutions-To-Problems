import re
from typing import Tuple
class Solution:
    def calculate(self, s: str) -> int:
        s = re.sub(" +", "", s)
        n = len(s)

        def f(i: int) -> Tuple[int, int]:
            output, op = 0, '+'
            while i < n and s[i] != ')':
                if s[i] in {"+", "-"}:
                    op = s[i]
                    i += 1

                if s[i] == '(':
                    i, num = f(i + 1)
                else:
                    num = 0
                    while i < n and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                output += -num if op == '-' else num

            return i + 1, output
        _, output = f(0)
        return output


# Checking in PyCharm/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.calculate(s = "1 + 1")  
    # s = "1 + 1" -> 2 
    # s = "(1+(4+5+2)-3)+(6+8)" -> 23
    # s = " 2-1 + 2 " -> 3
    print(Solve)
