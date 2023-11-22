class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        total_nums = len(nums)
        
        @cache
        def canPartitionFrom(index: int) -> bool:
            # Base case: If we've reached the end of the list, return True
            if index == total_nums:
                return True

            # Check for a pair of equal numbers
            if index + 1 < total_nums and nums[index] == nums[index + 1] and canPartitionFrom(index + 2):
                return True

            # Check for a triplet of equal numbers
            if index + 2 < total_nums and nums[index] == nums[index + 1] == nums[index + 2] and canPartitionFrom(index + 3):
                return True

            # Check for a triplet of consecutive numbers
            if index + 2 < total_nums and nums[index] + 1 == nums[index + 1] and nums[index + 1] + 1 == nums[index + 2] and canPartitionFrom(index + 3):
                return True

            return False

        return canPartitionFrom(0)
