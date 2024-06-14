class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment
        return moves

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 2, 1, 7]
    print(sol.minIncrementForUnique(nums))  # Output: 6
