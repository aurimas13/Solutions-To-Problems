class Solution:
    @staticmethod
    def removeDuplicates(s: str, k: int) -> str:
        s = list(s)
        counter = [1]
        n = len(s)
        stack = [s[0]]
        for i in range(1, n):
            if stack and s[i] == stack[-1]:
                counter.append(counter[-1]+1)
                stack.append(s[i])
            else:
                counter.append(1)
                stack.append(s[i])
            if counter[-1] == k:
                while counter[-1] != 1:
                    counter.pop(-1)
                    stack.pop(-1)
                counter.pop(-1)
                stack.pop(-1)
        return ''.join(stack)


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.removeDuplicates(s = "deeedbbcccbdaa", k = 3)
    # s = "deeedbbcccbdaa", k = 3 -> "aa"
    # s = "pbbcggttciiippooaais", k = 2 -> "ps"
    print(Solve)
