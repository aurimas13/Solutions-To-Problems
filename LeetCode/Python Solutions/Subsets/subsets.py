from typing import List


class Solution:
    def subsets(nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
    

# Driver Code
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution.subsets(nums))