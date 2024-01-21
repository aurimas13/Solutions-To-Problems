from typing import List
from heapq import heappop, heappush

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subsequences = []

        for num in nums:
            while subsequences and subsequences[0][0] + 1 < num:
                sub = heappop(subsequences)
                if sub[1] < 3:
                    return False

            if not subsequences or subsequences[0][0] == num:
                heappush(subsequences, [num, 1])  # end, len
            else:
                # Pop and push to maintain order
                sub = heappop(subsequences)
                sub[0] += 1
                sub[1] += 1
                heappush(subsequences, sub)

        while subsequences:
            sub = heappop(subsequences)
            if sub[1] < 3:
                return False

        return True


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isPossible(nums = [1,2,3,3,4,5])  # nums = [1,2,3,3,4,5] -> true | nums = [1,2,3,3,4,4,5,5] -> true
    print(Solve)