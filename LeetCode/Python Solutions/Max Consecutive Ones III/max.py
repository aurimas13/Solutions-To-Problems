from typing import List


class Solution:
    @staticmethod
    def longestOnes(nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0

        for right, num in enumerate(nums):
            if not num:
                zero_count += 1

            if zero_count > k:
                if not nums[left]:
                    zero_count -= 1
                left += 1

        return right - left + 1


# Checking in PyCharm/terminal
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2)  # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,
    # 0,1,1,1,1], k = 3 -> 10 | nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 -> 6
    print(Solve)