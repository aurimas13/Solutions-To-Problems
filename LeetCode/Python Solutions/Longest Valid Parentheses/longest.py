class Solution:
    def longestValidParentheses(self, s: str) -> int:
        bal = [-1]
        maxWin = 0
        validWin = 0
        for cind, c in enumerate(s):
            if c == '(':
                bal.append(cind)
            if c == ')':
                bal.pop()
                if len(bal) > 0:
                    validWin = cind - bal[-1]
                    maxWin = max(maxWin,validWin)
                else:
                    bal.append(cind)
        return maxWin


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestValidParentheses(s = ")()())")  # s = ")()())" -> 4 | s = "(()" -> 2 | s = "" -> 0
    print(Solve)
