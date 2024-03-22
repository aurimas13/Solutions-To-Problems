from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Initialize the answer array with 1s
        
        # Calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Calculate the product of all elements to the right of each element
        # and multiply it by the product calculated in the previous step
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer



# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.productExceptSelf(nums = [1,2,3,4])  # nums = [1,2,3,4] -> [24,12,8,6] | [-1,1,0,-3,3] -> [0,0,9,0,0]
    print(Solve)