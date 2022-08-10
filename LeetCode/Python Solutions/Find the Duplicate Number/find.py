from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sum(set(nums))
        n = sum(nums)
        return int((n - s) / (len(nums) - len(set(nums))))

# OR

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         bits = 0
#         for num in nums:
#             bit = 1 << num
#             if bits & bit:
#                 return num

#             bits |= bit

#         return -1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findDuplicate([1,3,4,2,2])  # [1,3,4,2,2] -> 2 | nums = [3,1,3,4,2] -> 3
    print(Solve)

