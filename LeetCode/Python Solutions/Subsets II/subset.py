from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list to group duplicate elements together
        nums.sort()

        # Initialize the result list with an empty subset
        result = [[]]

        # Iterate over the input list to build subsets
        for i in range(len(nums)):
            # If the current element is not a duplicate, start building new subsets from the previous ones
            if i == 0 or nums[i] != nums[i - 1]:
                prev_len = len(result)

            # Calculate the length of the result list
            curr_len = len(result)

            # Add the current element to each subset formed in the previous iteration
            result.extend([subset + [nums[i]] for subset in result[curr_len - prev_len:]])

        return result


# Test the solution
if __name__ == '__main__':
    sol = Solution()

    nums1 = [1, 2, 2]
    assert sorted(sol.subsetsWithDup(nums1)) == sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])

    nums2 = [0]
    assert sorted(sol.subsetsWithDup(nums2)) == sorted([[], [0]])

    nums3 = [4, 4, 4, 1, 4]
    assert sorted(sol.subsetsWithDup(nums3)) == sorted([[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])

    print("All tests passed.")
