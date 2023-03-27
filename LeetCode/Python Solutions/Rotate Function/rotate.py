from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Calculates the maximum sum of F(0), F(1), ..., F(n-1) where F(k) = 0 * B[0] + 1 * B[1] + ... + (n-1) * B[n-1]
        and B is a list obtained by rotating nums k times.

        :param nums: list of integers
        :return: maximum sum of F(0), F(1), ..., F(n-1)
        """

        # Calculate the sum of all elements in nums.
        total = sum(nums)

        # Calculate F(0) and store it in a variable.
        f = sum(i * num for i, num in enumerate(nums))

        # Initialize max_f as F(0).
        max_f = f

        # Calculate F(k) for k = 1, 2, ..., n-1.
        n = len(nums)
        for k in range(1, n):
            # F(k) = F(k - 1) + total - n * nums[n - k]
            f = f + total - n * nums[n - k]

            # Update max_f if the current F(k) is greater than max_f.
            max_f = max(max_f, f)

        return max_f

# Test the solution using the provided test case.
if __name__ == "__main__":
    s = Solution()
    nums = [4, 3, 2, 6]
    print(s.maxRotateFunction(nums))

