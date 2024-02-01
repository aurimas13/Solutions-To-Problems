class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()  # Sort the array first
        result = []
        
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] <= k:
                result.append(nums[i:i + 3])
            else:
                return []  # Condition not met, return an empty array
        
        return result
