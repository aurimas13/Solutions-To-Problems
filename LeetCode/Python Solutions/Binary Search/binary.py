from typing import List

class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.search(nums = [-1,0,3,5,9,12], target = 9)
    # nums = [-1,0,3,5,9,12], target = 9
    # -> 4
    print(Solve)
