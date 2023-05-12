from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_val, max_val, n = min(nums), max(nums), len(nums)

        # If all elements are the same, the maximum gap is 0.
        if min_val == max_val:
            return 0

        # Calculate the size and count of buckets.
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Initialize the buckets.
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        # Place the numbers in the appropriate buckets.
        for num in nums:
            index = (num - min_val) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        # Remove empty buckets.
        buckets = [bucket for bucket in buckets if bucket != [float('inf'), float('-inf')]]

        # Calculate the maximum gap between adjacent buckets.
        max_gap = 0
        prev_max = buckets[0][1]
        for i in range(1, len(buckets)):
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]

        return max_gap
    

# Tests:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maximumGap(nums = [3,6,9,1])  
    # nums = [3,6,9,1] -> 3
    # nums = [10] -> 0
    print(Solve)
