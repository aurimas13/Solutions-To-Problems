from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        immediate = [{""}]
        for i in range(1, n + 1):
            cur = set()
            for each in immediate[-1]:
                cur.add("(" + each + ")")
            for j in range(1, i):
                for l in immediate[j]:
                    for r in immediate[i - j]:
                        cur.add(l + r)
            immediate.append(cur)
        return list(immediate[-1])


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.generateParenthesis(n=3)  # n=1 -> ["()"] | n=3 -> ["((()))","(()())","(())()","()(())","()()()"]
    print(Solve)

