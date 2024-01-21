import java.util.Arrays;

class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, right = 0;
        long total = 0;
        int maxFreq = 0;

        for (right = 0; right < nums.length; right++) {
            total += nums[right];

            // Check if the total increments needed is more than k
            while ((long) nums[right] * (right - left + 1) > total + k) {
                total -= nums[left];
                left++;
            }

            maxFreq = Math.max(maxFreq, right - left + 1);
        }

        return maxFreq;
    }
}
