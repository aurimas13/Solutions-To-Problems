class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Initialize the result array with zeros
        left, right = 0, n - 1  # Two pointers
        for i in range(n - 1, -1, -1):  # Fill the result array from the end
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
