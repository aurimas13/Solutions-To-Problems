from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        for i, val1 in enumerate(nums):
            seen = set()
            if val1 not in dups:
                dups.add(val1)
                for val2 in nums[i+1:]:
                    complement = -val1 - val2
                    if complement in seen:
                        res.add(tuple(sorted((val1, val2, complement))))
                    else:
                        seen.add(val2)
        return res


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.threeSum([-1,0,1,2,-1,-4])  # nums = [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    print(Solve)
