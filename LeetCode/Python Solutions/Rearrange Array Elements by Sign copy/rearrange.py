class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative numbers while preserving their order
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        
        # Merge positive and negative numbers by alternating, starting with positive
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        
        return result
