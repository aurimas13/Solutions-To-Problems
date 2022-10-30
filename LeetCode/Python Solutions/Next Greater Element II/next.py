from typing import List

class Solution:
    @staticmethod
    def nextGreaterElements(nums: List[int]) -> List[int]:
        stack, res, n = [], [-1]*len(nums), len(nums)
        for i in range(0, 2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                top = stack.pop()
                if res[top] == -1:
                    res[top] = nums[i%n]
            stack.append(i%n)
        return res

# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.nextGreaterElements(nums=[1, 2, 3, 4, 3])  # nums = [1,2,3,4,3] -> [2,3,4,-1,4] | nums = [1,2,1] -> [2,-1,2]
    print(Solve)
