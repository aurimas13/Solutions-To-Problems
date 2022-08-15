from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        notes:
            zeros in the array would immeditale reset the streak
            negatives could re negate them

        i can store two dp arrays
        dp max will store the max up to this points
        dp min will store the min up this point
        '''
        N = len(nums)
        dp_max = [0] * N
        dp_min = [0] * N

        dp_max[0] = dp_min[0] = nums[0]

        ##first pass, find min and max at each pointin the array
        for i in range(1, N):
            dp_max[i] = max(nums[i] * dp_max[i - 1], nums[i], dp_min[i - 1] * nums[i])
            dp_min[i] = min(nums[i] * dp_min[i - 1], nums[i], dp_max[i - 1] * nums[i])

        ##second pass, find the max that could be obtained at each point using the two dp
        maxes = [0] * N
        ##starting off take max of the beginning

        for i in range(N):
            maxes[i] = max(dp_max[i], dp_min[i])

        return max(maxes)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.maxProduct([2,3,-2,4])  # nums = [2,3,-2,4] -> 6 | [-2,0,-1 -> 0
    print(Solve)
