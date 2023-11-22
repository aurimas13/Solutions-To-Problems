from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        i = -1
        for num in nums:
            index = bisect_left(nums, x=num, lo=0, hi=i + 1)
            if index == i + 1:
                i += 1
            nums[index] = num
        return i + 1


# Tests:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.lengthOfLIS(nums = [0,1,0,3,2,3])  # nums = [0,1,0,3,2,3] -> 4
    print(Solve)

# OR

# # we have two decisions at each nums value
# # add to sequence or don't add to sequence
# # we can build the whole tree with sub problems and
# # take the maximum value of the substring
# dp = [1] * len(nums)
# max_len = 1
# # want to iterate through all the possible ending positions, the subproblems
# for i in range(1, len(nums)):
#     # want to parse up to the ith character adding values less along the way
#     for j in range(i):
#         i_val = nums[i]
#         j_val = nums[j]
#         # we use our memo here to test if we should add this character based off previous values
#         # or not
#         if i_val > j_val:
#             # if i is greater than that value we can add
#             # so we take the maximum sub_string length here we have found
#             # this ensures we are getting the maximum sub-string
#             dp[i] = max(dp[i], dp[j] + 1)
#             if dp[i] > max_len:
#                 max_len = dp[i]
# # we can then return the maximum substring through the list
# return max_len
