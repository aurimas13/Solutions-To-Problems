class Solution:
    def decodeString(self, s: str) -> str:
        times = []
        stack = [[]]
        k = 0
        for c in s:
            if c.isnumeric():
                k = int(c) + 10 * k
            elif c == '[':
                times.append(k)
                stack.append([])
                k = 0
            elif c == ']':
                stack[-2].extend(times[-1] * stack[-1])
                times.pop()
                stack.pop()
            else:
                stack[-1].append(c)

        return "".join(stack[0])

# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.decodeString(s = "3[a]2[bc]") # s = "3[a]2[bc]" -> aaabcbc | s = "3[a2[c]]" ->  "ccaccacc
    print(Solve)
