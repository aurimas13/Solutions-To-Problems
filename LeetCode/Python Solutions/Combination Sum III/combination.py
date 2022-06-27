from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, combination, next_start):
            if remain == 0 and len(combination) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(combination))
                return
            elif remain < 0 or len(combination) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                combination.append(i+1)
                backtrack(remain-i-1, combination, i+1)
                # backtrack the current choice
                combination.pop()

        backtrack(n, [], 0)

        return results
# Checking in PyCharm/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.combinationSum3(3, 9)  # [3, 9] -> [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    print(Solve)