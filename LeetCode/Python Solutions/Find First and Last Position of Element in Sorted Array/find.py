from typing import List


class Solution:
    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = None
        right = None

        def find(start, end, side=False):
            left = None
            right = None
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    if not side or side == "left":
                        left, _ = find(start, mid - 1, 'left')
                        if left == -1:
                            left = mid
                    if not side or side == 'right':
                        _, right = find(mid + 1, end, 'right')
                        if right == -1:
                            right = mid
                    return [left, right]
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return [-1, -1]

        return find(0, n - 1)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.searchRange(nums = [5,7,7,8,8,10],  target = 8)  # nums = [5,7,7,8,8,10], target = 6 -> [-1,-1] | nums = [5,7,7,8,8,10],
    # target = 8 -> [3,4]
    print(Solve)
