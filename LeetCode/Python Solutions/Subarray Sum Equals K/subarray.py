from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        preSum, ret, size = [0], 0, len(nums)
        count = Counter(preSum)
        if size == 1:
            return 1 if nums[0] == k else 0
        for val in nums:
            s = preSum[-1] + val
            preSum.append(s)
            ret += count.get(s - k, 0)
            count[s] = count.get(s, 0) + 1

        return ret

# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.subarraySum(nums = [1,1,1], k = 2 ) # nums = [1,1,1], k = 2 -> 2 | nums = [1,2,3], k = 3 -> 2
    print(Solve)