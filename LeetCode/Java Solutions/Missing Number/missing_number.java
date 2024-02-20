class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)  # Initialize missing to n since we'll XOR with numbers from 0 to n
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
