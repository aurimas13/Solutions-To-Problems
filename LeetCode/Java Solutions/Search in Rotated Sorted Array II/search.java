from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> bool:
        set_num = set(nums)
        if target in set_num:
            return True
        else:
            return False


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.search(nums = [2,5,6,0,0,1,2], target = 0)
    # nums = [2,5,6,0,0,1,2], target = 0 -> true
    # nums = [2, 5, 6, 0, 0, 1, 2], target = 3 -> false
    print(Solve)
