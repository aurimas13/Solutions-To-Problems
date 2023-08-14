import java.util.Arrays;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Sort the array in ascending order
        Arrays.sort(nums);
        
        // Return the kth largest element
        return nums[nums.length - k];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test the solution
        int result = solution.findKthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2);  // Expected output: 5
        System.out.println(result);
        
        result = solution.findKthLargest(new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4);  // Expected output: 4
        System.out.println(result);
    }
}
