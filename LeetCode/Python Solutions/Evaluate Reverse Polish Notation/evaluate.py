from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack for storing numbers and results
        stack = []

        # Define a set of supported operators
        operators = {"+", "-", "*", "/"}

        # Iterate through the tokens
        for token in tokens:
            if token in operators:
                # Pop the last two numbers from the stack
                num2 = stack.pop()
                num1 = stack.pop()

                # Evaluate the expression using the operator
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                else:
                    result = int(num1 / num2)

                # Push the result back onto the stack
                stack.append(result)
            else:
                # Push the number onto the stack
                stack.append(int(token))

        # The final result is the last item in the stack
        return stack[-1]

if __name__ == "__main__":
    solution = Solution()
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print("All tests passed.")
