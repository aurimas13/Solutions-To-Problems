from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,_maxs = 0,len(height) - 1,0
        while l < r:
            _maxs = max((r - l) * min(height[l],height[r]),_maxs)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return _maxs


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.maxArea([1,8,6,2,5,4,8,3,7])  # height = [1,8,6,2,5,4,8,3,7] -> 49
    print(Solve)


# OR
#
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         maxarea = 0
#         for left in range(len(height)):
#             for right in range(left + 1, len(height)):
#                 width = right - left
#                 maxarea = max(maxarea, min(height[left], height[right]) * width)
#
#         return maxarea
#
# OR
#
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         maxarea = 0
#         left = 0
#         right = len(height) - 1
#
#         while left < right:
#             width = right - left
#             maxarea = max(maxarea, min(height[left], height[right]) * width)
#             if height[left] <= height[right]:
#                 left += 1
#             else:
#                 right -= 1
#
#         return maxarea