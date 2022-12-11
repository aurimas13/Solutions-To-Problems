from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        n = [0] * (len(nums1) + len(nums2))
        li, ri, i = 0, 0, 0
        while (li < len(nums1) and ri < len(nums2)):
            if nums1[li] < nums2[ri]:
                n[i] = nums1[li]
                li += 1
            else:
                n[i] = nums2[ri]
                ri += 1
            i += 1

        if li != len(nums1):
            n[i:] = nums1[li:]
        else:
            n[i:] = nums2[ri:]
        m = len(n)

        if len(n) % 2 != 0:
            return float(n[(m + 1) // 2 - 1])
        return (n[(m // 2 - 1)] + n[(m // 2 + 1 - 1)]) / 2


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])
    # nums1 = [1,3], nums2 = [2] -> 2.00000
    # nums1 = [1,2], nums2 = [3,4] -> 2.50000
    print(Solve)
