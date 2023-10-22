import java.util.*;

public class Solution {
    public int maximumScore(int[] nums, int k) {
        // Initialize the maximum score, left pointer, and right pointer
        int maxScore = nums[k];
        int currMin = nums[k];
        int left = k;
        int right = k;

        // Iterate until the left and right pointers reach the ends of the array
        while (left > 0 || right < nums.length - 1) {
            // Choose the direction to move (left or right)
            if (left == 0) {
                right++;
            } else if (right == nums.length - 1) {
                left--;
            } else if (nums[left - 1] > nums[right + 1]) {
                left--;
            } else {
                right++;
            }

            // Update the current minimum element and maximum score
            currMin = Math.min(currMin, Math.min(nums[left], nums[right]));
            maxScore = Math.max(maxScore, currMin * (right - left + 1));
        }

        return maxScore;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        System.out.println(solution.maximumScore(new int[]{1, 4, 3, 7, 4, 5}, 3));  // Output: 15
        // Test case 2
        System.out.println(solution.maximumScore(new int[]{5, 5, 4, 5, 4, 1, 1, 1}, 0));  // Output: 20
        // Test case 3
        System.out.println(solution.maximumScore(new int[]{5, 5, 4, 1, 4, 1, 1, 1}, 3));  // Output: 16
    }
}
