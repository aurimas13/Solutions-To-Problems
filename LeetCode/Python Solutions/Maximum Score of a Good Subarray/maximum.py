from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Initialize the maximum score and the current minimum element
        max_score = nums[k]
        curr_min = nums[k]
        
        # Iterate through the subarrays that include nums[k]
        for i in range(k, -1, -1):
            # Update the current minimum element
            curr_min = min(curr_min, nums[i])
            
            # Update the maximum score by extending the subarray to the right
            for j in range(k + 1, len(nums) + 1):
                # Calculate the score of the current subarray
                score = curr_min * (j - i)
                
                # Update the maximum score
                max_score = max(max_score, score)
                
                # Break the loop if we reach the end of the array
                if j == len(nums) or nums[j] < curr_min:
                    break
                    
        return max_score


# Checking in terminal/console:
if __name__ == '__main__':
    # Test cases
    solution = Solution()

    # Test case 1
    print(solution.maximumScore([1, 4, 3, 7, 4, 5], 3))  # Output: 15
    # Test case 2
    print(solution.maximumScore([5, 5, 4, 5, 4, 1, 1, 1], 0))  # Output: 20
    # Test case 3
    print(solution.maximumScore([5, 5, 4, 1, 4, 1, 1, 1], 3))  # Output: 16
