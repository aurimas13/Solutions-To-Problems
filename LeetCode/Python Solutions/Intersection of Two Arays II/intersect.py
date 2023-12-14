from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1) & Counter(nums2)
        answer = []
        for k, v in counts.items():
            answer.extend([k] * v)
        return answer


# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.intersect([1,2,2,1], [2,2])  #  [1,2,2,1], [2,2] -> [2, 2] | [4,9,5], [9,4,9,8,4] -> [4, 9]
    print(Solve)
