from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.intersection([4,9,5], [9,4,9,8,4])  #  [1,2,2,1], [2,2] -> 2 | [4,9,5], [9,4,9,8,4] -> [4, 9]
    print(Solve)

