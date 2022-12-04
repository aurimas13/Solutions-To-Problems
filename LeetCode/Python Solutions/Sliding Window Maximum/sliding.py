from collections import deque
from typing import List


class Solution:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) < k:
            raise ValueError()

        window = deque()
        res = []
        for i in range(len(nums)):
            while window and (i - k) >= window[0][1]:
                window.popleft()

            while window and (nums[i] >= window[-1][0]):
                window.pop()

            window.append((nums[i], i))

            if window and i >= k - 1:
                res.append(window[0][0])

        return res


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3 )
    # nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
    # nums = [1], k = 1 -> [1]
    print(Solve)


# # Alternative method:
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if not nums or len(nums) < k:
#             raise ValueError()
#
#         n = len(nums)
#         left, right = [0] * (n + 1), [0] * (n + 1)
#         left[-1], right[-1] = float('-inf'), float('-inf')
#
#         for i,j in zip(range(0, n), reversed(range(0, n))):
#             left[i] = nums[i] if i % k == 0 else max(left[i-1], nums[i])
#             right[j] = nums[j] if (j + 1) % k == 0 else max(right[j+1], nums[j])
#
#         res = []
#         for i in range(n - k + 1):
#             res.append(max(left[i + k - 1], right[i]))
#
#         return res
