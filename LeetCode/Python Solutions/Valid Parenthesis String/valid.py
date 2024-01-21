class Solution:
    @staticmethod
    def checkValidString(s: str) -> bool:
        # CC O(n), SC O(n)
        stack = []
        star = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)

        while star and stack and star[-1] > stack[-1]:
            star.pop()
            stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.checkValidString(s = "(*))")  # s = "(*))" -> True
    print(Solve)
