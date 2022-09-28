from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = sorted(nums)
        l = len(nums)
        return n[l-k]


# Checking in PyCharm/terminal
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)  #  nums = [3,2,1,5,6,4], k = 2 -> 5 | nums = [3,2,3,1,2,4,5,5,6], k = 4 -> 4
    print(Solve)
