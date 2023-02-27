from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Sort the array in non-increasing order
        nums.sort(reverse=True)
        
        # Loop through the array to find the value of x
        for x in range(len(nums)+1):
            count = 0
            for i in range(len(nums)):
                if nums[i] >= x:
                    count += 1
                else:
                    break
            if count == x:
                return x
        
        # If x is not found, return -1
        return -1


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]) 
    # nums = [3,5] -> 2
    # nums = [0,0] -> -1
    print(Solve)
    