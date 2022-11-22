from typing import List


class Solution:
    @staticmethod
    def canPartition(nums: List[int]) -> bool:
        target = sum(nums)
        if target%2 != 0:
            return False
        target = target//2
        dp={0}

        for i in range(len(nums)):
            dp.update([k+nums[i] for k in dp])
            if target in dp:
                return True
        return False
        return triangle


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.canPartition(nums = [1, 5, 11, 5])
    # nums = [1, 5, 11, 5] -> true
    # nums = [1,2,3,5] -> false
    print(Solve)
