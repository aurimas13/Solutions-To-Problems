from typing import List


class Solution:
    @staticmethod
    def canCross(stones: List[int]) -> bool:
        seen = set()
        stoneSet = set(stones)
        end = stones[-1]
        stack = [(0, 0)]
        while len(stack) > 0:
            loc, steps = stack.pop()
            if (loc, steps) in seen:
                continue
            seen.add((loc, steps))
            if loc == end:
                return True
            elif loc < end:
                for i in range(steps-1, steps+2):
                    if i <= 0:
                        continue
                    if loc + i in stoneSet:
                        stack.append((loc+i, i))
        return False


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17]) # stones = [0,1,3,5,6,8,12,17] -> True | stones = [0,1,2,3,4,8,9,11] -> False
    print(Solve)
