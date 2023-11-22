from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (2*sum(set(nums)) - sum(nums))


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.singleNumber([4,1,2,1,2])  # [2,2,1] -> 1 | [4,1,2,1,2] -> 4
    print(Solve)

