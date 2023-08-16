import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // Handle edge cases
        if (nums == null || nums.length < k) {
            throw new IllegalArgumentException("Invalid input.");
        }

        // Initialize deque (double-ended queue) and result array
        Deque<int[]> window = new LinkedList<>();
        int[] res = new int[nums.length - k + 1];

        // Iterate through the input array
        for (int i = 0; i < nums.length; i++) {
            // Remove elements that are out of the current sliding window from the front of the deque
            while (!window.isEmpty() && (i - k) >= window.peekFirst()[1]) {
                window.pollFirst();
            }

            // Remove elements smaller than the current element from the back of the deque
            while (!window.isEmpty() && nums[i] >= window.peekLast()[0]) {
                window.pollLast();
            }

            // Append the current element and its index to the deque
            window.addLast(new int[]{nums[i], i});

            // Append the maximum element of the current sliding window to the result array
            if (i >= k - 1) {
                res[i - k + 1] = window.peekFirst()[0];
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Call the 'maxSlidingWindow' method with the input array and window size
        int[] result1 = solution.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3);  // Expected output: [3, 3, 5, 5, 6, 7]
        int[] result2 = solution.maxSlidingWindow(new int[]{1}, 1);  // Expected output: [1]
        int[] result3 = solution.maxSlidingWindow(new int[]{1, -1}, 1);  // Expected output: [1, -1]
        int[] result4 = solution.maxSlidingWindow(new int[]{9, 11}, 2);  // Expected output: [11]
        int[] result5 = solution.maxSlidingWindow(new int[]{4, -2, -8, 5, -2, 7, 7, 2, -6, 5}, 4);  // Expected output: [5, 5, 7, 7, 7]

        // Print the results
        for (int val : result1) System.out.print(val + " ");
        System.out.println();
        for (int val : result2) System.out.print(val + " ");
        System.out.println();
        for (int val : result3) System.out.print(val + " ");
        System.out.println();
        for (int val : result4) System.out.print(val + " ");
        System.out.println();
        for (int val : result5) System.out.print(val + " ");
    }
}
