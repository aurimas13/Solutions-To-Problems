class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        ope = "+"
        
        if not s:
            return 0
        
        operators = set(['+', '-', '*', '/'])
        nums = set([str(x) for x in range(0, 10)])

        for i in range(len(s)):
            char = s[i]

            if char in nums:
                curr = curr * 10 + int(char)

            if char in operators or i == len(s) - 1:
                if ope == '+':
                    stack.append(curr)

                elif ope == '-':
                    stack.append(-curr)

                elif ope == '*':
                    stack[-1] *= curr

                elif ope == '/':
                    stack[-1] = int(stack[-1] / curr)

                curr = 0
                ope = char

        return sum(stack)



# Checking in Terminal/Console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.calculate(" 3+5 / 2 ")  
    # s = "3+2*2" -> 7  
    # s = " 3+5 / 2 " -> 5
    print(Solve)


