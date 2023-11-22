from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # remove any zeros from nums, as they do not matter
        pruned_nums = []
        max_num = None
        for num in nums:
            if num != 0:
                pruned_nums.append(num)
                if max_num is None:
                    max_num = num
                else:
                    max_num = max(max_num, num)
        nums = pruned_nums

        # if, after removing all zeros, nums is empty, then nums only contained zeros, so the answer is zero
        if len(nums) == 0:
            return 0

        # if, after removing all zeros, the length of nums is less than or equal to m,
        # then we can split nums so that each subarray is length one
        # in which case, the max val is the max val of nums
        if m >= len(nums):
            return max_num

        # initialize the prefix sum array
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # initialize the table
        answer_table = [prefix_sum]
        for i in range(1, m):
            answer_table.append([None] * len(nums))

        # iterate across number of subarray partitions, i
        for i in range(1, m):

            # index of the prefix array for which we are computing the min partition val (i partitions)
            prefix_index = i

            # index of the rightmost partition of the prefix array
            # prefix is <= r_part_index,  suffix is > r_part_index
            r_part_index = i - 1

            # iterate through each possible prefix length
            while prefix_index < len(nums):

                # initialize the min partition value
                v_suffix = prefix_sum[prefix_index] - prefix_sum[r_part_index]
                v_prefix = answer_table[i - 1][r_part_index]

                min_val = max(v_suffix, v_prefix)

                # iterate through partition indices until we hit end of prefix, or until we can't optimize further
                while r_part_index < prefix_index:
                    v_suffix = prefix_sum[prefix_index] - prefix_sum[r_part_index]
                    v_prefix = answer_table[i - 1][r_part_index]

                    # if moving the rightmost partition index would increase the min partition value, break
                    if min_val < max(v_prefix, v_suffix):
                        break

                    # otherwise, it could improve further
                    else:
                        min_val = max(v_prefix, v_suffix)

                    r_part_index += 1

                # since we terminated the loop one step past the minimum, move a single step back
                r_part_index -= 1

                # update the table
                answer_table[i][prefix_index] = min_val

                prefix_index += 1

        return answer_table[-1][-1]


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.splitArray(nums = [7,2,5,10,8], m = 2)  # nums = [7,2,5,10,8], m = 2 -> 18 | nums = [1,2,3,4,5], m = 2 -> 9
    print(Solve)
