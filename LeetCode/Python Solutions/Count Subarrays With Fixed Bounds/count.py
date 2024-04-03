class Solution:
    def countSubarrays(self, nums, minK, maxK) -> int:
        lastMin, lastMax, lastInvalid, count = -1, -1, -1, 0
        for i, num in enumerate(nums):
            # Update the last seen positions for minK and maxK
            if num == minK: lastMin = i
            if num == maxK: lastMax = i
            # Invalidate the segment if the number is out of bounds
            if num < minK or num > maxK: lastInvalid = i
            # Add to count the number of valid subarrays ending at i
            count += max(0, min(lastMin, lastMax) - lastInvalid)
        return count
