from typing import List


class Solution:
    @staticmethod
    def thirdMax(nums: List[int]) -> int:
        result = sorted(set(nums))
        if len(result) <= 2:
            return max(nums)
        else:
            return result[::-1][2]


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.thirdMax(nums = [3,2,1])
    # nums = [3,2,1] -> 1
    # nums = [1, 2] -> 2
    print(Solve)
