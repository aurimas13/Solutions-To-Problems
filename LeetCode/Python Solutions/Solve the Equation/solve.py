class Solution:
    @staticmethod
    def solveEquation(equation: str) -> str:
        # move all the xs and numbers to left, sum up the xs' coeffients and numbers
        coeff, sum_ = 0, 0
        op = '+'
        is_left = True
        i = 0
        # sum up before last operator
        for j, c in enumerate(equation):
            if c == '+' or c == '-' or c == '=':
                if j > 0 and equation[j - 1] != '=':
                    multipler = 1 if is_left ^ (op == '-') else -1
                    if equation[j - 1] == 'x':
                        cur_coeff = int(equation[i: j - 1]) if j - 1 > i else 1
                        coeff += multipler * cur_coeff
                    else:
                        sum_ += multipler * int(equation[i:j])

                if c == '=':
                    is_left = False
                op = c if c != '=' else '+'
                i = j + 1

        # sum up after last operator
        multipler = 1 if op == '-' else -1
        if equation[-1] == 'x':
            cur_coeff = int(equation[i:-1]) if i < len(equation) - 1 else 1
            coeff += multipler * cur_coeff
        else:
            sum_ += multipler * int(equation[i:])

        if sum_ == 0:
            if coeff != 0:
                return "x=0"
            else:
                return "Infinite solutions"
        else:
            if coeff == 0:
                return "No solution"
            else:
                return f"x={-sum_ // coeff}"


# Checking in console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.solveEquation(equation = "x+5-3+x=6+x-2")
    # equation = "2x=x" -> "x=0"
    # equation = "x+5-3+x=6+x-2" -> "x=2"
    # equation = "x=x" -> "Infinite solutions"
    print(Solve)
