from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results

# or

# class Solution:
#     @staticmethod
#     def fourSum(nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         output = []
#         if len(nums) == 0:
#             return []
#         if len(nums) == 4:
#             if sum(nums) == target:
#                 return [nums]
#             else:
#                 return []
#         for i in range(len(nums) - 3):
#             for j in range(i + 1, len(nums) - 2):
#                 lo, hi = j + 1, len(nums) - 1
#                 while lo < hi:
#                     sum1 = nums[i] + nums[j] + nums[lo] + nums[hi]
#                     if i != j and j != lo and i != lo and j != hi and i != hi \
#                             and abs(sum1 - target) == 0 and \
#                             sorted([nums[i], nums[j], nums[lo], nums[hi]]) \
#                             not in output:
#                         output.append(sorted([nums[i], nums[j], nums[lo], nums[hi]]))
#                     if sum1 < target:
#                         lo += 1
#                     else:
#                         hi -= 1
#         return output

# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)
    # nums = [1,0,-1,0,-2,2],  target = 0
    # -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(Solve)
