from typing import List


class Solution:
    @staticmethod
    def checkSubarraySum(nums: List[int], k: int) -> bool:
        # index 0 has sum % k equal to 0
        memo = {0: 0}
        local_sum = 0

        for index in range(len(nums)):
            local_sum += nums[index]

            # check if we've seen this remainder before
            calculation = local_sum % k
            if calculation not in memo:
                # mark the place where we saw this remainder
                memo[calculation] = index + 1
            elif memo[calculation] < index:
                # we've seen this remainder before, and it was at lesat 1 away (size 2)
                # seeing the same remainder twice means that the difference is a multiple of k
                # ex:   k = 3
                #   nums:         [(0) 4, 7,  1,  1]
                #   running_sum:   (0) 4  11  12  13
                #   modulo 3:      (0) 1  2   0   1
                #                   ^         ^
                #                    therefore 4,7,1 is divisible by 3, or a multiple of 3
                #                      ^           ^
                #               (and so is 7,1,1 since modulo 1 is repeated)
                return True
        return False


# Check in the PyCharm/terminal:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6)
    # nums = [23,2,4,6,7], k = 6 -> true
    # nums = [23,2,6,4,7], k = 6 -> true
    # nums = [23,2,6,4,7], k = 13 -> false
    print(Solve)
