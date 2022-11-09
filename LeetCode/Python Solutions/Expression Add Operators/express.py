from typing import List


class Solution:
    @staticmethod
    def addOperators(num: str, target: int) -> List[str]:
        def calculate(pos, res, pre, value, expression):
            if pos == len(num):
                if target == value:
                    res.append(''.join(expression))
                return
            for j in range(pos, len(num)):
                number = num[pos: j + 1]
                if number[0] == '0' and j - pos > 0:
                    break
                number = int(number)
                if pos == 0:
                    calculate(j + 1, res, number, number, expression + [str(number)])
                    continue
                # add
                calculate(j + 1, res, number, value + number, expression + ['+'] + [str(number)])
                # subtract
                calculate(j + 1, res, -number, value - number, expression + ['-'] + [str(number)])
                # multiply
                calculate(j + 1, res, pre * number,
                          value - pre + pre * number, expression + ['*'] + [str(number)])

        result = []
        calculate(0, result, None, 0, [])
        return result


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.addOperators(num = "232", target = 8)
    # num = "232", target = 8 -> ["2*3+2","2+3*2"]
    print(Solve)
