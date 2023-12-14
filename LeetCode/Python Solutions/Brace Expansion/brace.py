from typing import List
from collections import deque


class Solution:
    @staticmethod
    def expand(s: str) -> List[str]:
        queue = deque()
        queue.append(s)
        result = []

        while queue:
            curr = queue.popleft()
            if '{' not in curr:
                result.append(curr)
            else:
                start = curr.index('{')
                end = curr.index('}')
                options = curr[start + 1:end].split(',')
                for option in options:
                    queue.append(curr[:start] + option + curr[end + 1:])

        return sorted(result)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.expand(s = "{a,b}c{d,e}f")
    # s = "{a,b}c{d,e}f" -> ["acdf","acef","bcdf","bcef"]
    # s = "abcd" -> ["abcd"]
    print(Solve)
