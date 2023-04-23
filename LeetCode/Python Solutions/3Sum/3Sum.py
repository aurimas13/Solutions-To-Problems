from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Set up two sets: one for storing results, the other for storing duplicates
        res, dups = set(), set()

        # Enumerate nums list and search for all values of it that sum to 0
        for i, val1 in enumerate(nums):
            # Initialize a new set for that particular index and val1
            seen = set()

            # Check if val1 is unique and the addition of other values gives a zero
            if val1 not in dups:
                dups.add(val1)

                # Loop over val2 in nums list, starting from one index ahead
                for val2 in nums[i + 1:]:
                    # Calculate the complement of val1 and val2
                    complement = -val1 - val2

                    # Check if the complement exists in the seen set
                    if complement in seen:
                        # If it does, we can have triplets that sum to zero
                        # Add this to the res set as a possible solution
                        res.add(tuple(sorted((val1, val2, complement))))
                    else:
                        # If not, add val2 to the seen set
                        seen.add(val2)

        return [list(triplet) for triplet in res]


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"nums": [-1, 0, 1, 2, -1, -4]}, [[-1, -1, 2], [-1, 0, 1]]),
        ({"nums": [0, 0, 0, 0]}, [[0, 0, 0]]),
        ({"nums": [1, 2, -2, -1]}, []),
        ({"nums": []}, []),
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.threeSum(**test_input)
        assert all(triplet in result for triplet in expected_output) and len(result) == len(expected_output), f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
