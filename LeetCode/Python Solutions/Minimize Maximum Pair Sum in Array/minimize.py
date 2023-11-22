class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array
        n = len(nums)
        maxPairSum = 0

        # Pair the smallest element with the largest, and so on.
        for i in range(n // 2):
            maxPairSum = max(maxPairSum, nums[i] + nums[n - 1 - i])

        return maxPairSum
