class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        int lastMin = -1, lastMax = -1, lastInvalid = -1;
        long count = 0;
        for (int i = 0; i < nums.length; i++) {
            // Update the last seen positions for minK and maxK
            if (nums[i] == minK) lastMin = i;
            if (nums[i] == maxK) lastMax = i;
            // Invalidate the segment if the number is out of bounds
            if (nums[i] < minK || nums[i] > maxK) lastInvalid = i;
            // Add to count the number of valid subarrays ending at i
            count += Math.max(0, Math.min(lastMin, lastMax) - lastInvalid);
        }
        return count;
    }
}
