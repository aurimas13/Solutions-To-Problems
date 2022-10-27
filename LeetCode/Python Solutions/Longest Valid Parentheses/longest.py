class Solution:
    @staticmethod
    def longestValidParentheses(s: str) -> int:
        bal = [-1]
        maxWin = 0
        validWin = 0
        for find, c in enumerate(s):
            if c == '(':
                bal.append(find)
            if c == ')':
                bal.pop()
                if len(bal) > 0:
                    validWin = find - bal[-1]
                    maxWin = max(maxWin,validWin)
                else:
                    bal.append(find)
        return maxWin


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestValidParentheses(s = ")()())")  # s = ")()())" -> 4 | s = "(()" -> 2 | s = "" -> 0
    print(Solve)
