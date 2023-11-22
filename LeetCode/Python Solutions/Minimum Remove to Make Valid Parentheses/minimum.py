from collections import deque


class Solution:
    @staticmethod
    def minRemoveToMakeValid(s: str) -> str:
        stack = deque()
        indexes_to_remove = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')' and not stack:
                indexes_to_remove.add(i)
            elif c == ')':
                stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack))
        res = [x for i, x in enumerate(s) if i not in indexes_to_remove]
        return ''.join(res)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minRemoveToMakeValid(s = "lee(t(c)o)de)" )
    # s = "lee(t(c)o)de)" -> "lee(t(c)o)de"
    # s = "a)b(c)d" -> "ab(c)d"
    print(Solve)
