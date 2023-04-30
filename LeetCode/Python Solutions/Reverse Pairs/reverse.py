from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(nums, low, high):
            if low >= high:
                return 0

            mid = low + (high - low) // 2
            count = merge_sort(nums, low, mid) + merge_sort(nums, mid + 1, high)

            # Count the number of pairs where the left and right subarrays are sorted
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge the two sorted subarrays
            nums[low:high + 1] = sorted(nums[low:high + 1])

            return count

        return merge_sort(nums, 0, len(nums) - 1)
    
if __name__ == "__main__":
    
    assert Solution().reversePairs([1, 3, 2, 3, 1]) == 2
    assert Solution().reversePairs([2, 4, 3, 5, 1]) == 3
    assert Solution().reversePairs([5, 4, 3, 2, 1]) == 4
    assert Solution().reversePairs([1, 2, 3, 4, 5]) == 0
    assert Solution().reversePairs([1, 1, 1, 1, 1]) == 0

    print("All tests passed.")