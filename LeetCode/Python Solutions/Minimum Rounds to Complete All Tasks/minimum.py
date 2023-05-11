from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks).values()
        # If there is, return -1 as it is not possible to complete
        # such a task in a round as we can complete either 2 or 3 tasks
        # of the same difficulty level in a round.
        # Calculate the minimum rounds needed to complete tasks of each
        # difficulty level. The calculation (c + 2)//3 gives the rounded up
        # integer division of c by 3 which is equivalent to math.ceil(c / 3.0).
        # Sum up the minimum rounds for all task difficulty levels.
        return -1 if 1 in counts else sum((c + 2)//3 for c in counts)


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumRounds([2,2,3,3,2,4,4,4,4,4]) == 4
    assert solution.minimumRounds([7,7,7,7,7,7]) == 2
    assert solution.minimumRounds([5,5,5,5]) == 2
    assert solution.minimumRounds([2,3,3]) == -1
    print("All tests passed.")
