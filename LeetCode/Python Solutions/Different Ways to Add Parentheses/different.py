from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Base case: expression is a number
        if expression.isdigit():
            return [int(expression)]

        # Split the expression into numbers and operators
        results = []
        for i, c in enumerate(expression):
            if c in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if c == "+":
                            results.append(l + r)
                        elif c == "-":
                            results.append(l - r)
                        elif c == "*":
                            results.append(l * r)

        return results


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.diffWaysToCompute(expression = "2-1-1")
    # expression = "2-1-1" -> [0,2]
    # expression = "2*3-4*5" -> [-34,-14,-10,-10,10]
    print(Solve)