from typing import List
import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = sorted(t for t in zip(nums, range(n)))
        ans = [0] * n
        smaller = []
        for _, i in nums:  # value, original index
            idx = bisect.bisect(smaller, i)
            ans[i] = len(smaller)-idx
            smaller.insert(idx, i)
        return ans


# Checking in PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countSmaller([5,2,6,1])  # nums = [5,2,6,1] -> [2,1,1,0]
    print(Solve)
