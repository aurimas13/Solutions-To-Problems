import java.util.Arrays;

public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = {-1, -1};

        // Find the first occurrence of target using binary search
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        res[0] = left;

        // Find the last occurrence of target using binary search
        right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        res[1] = right;

        // Check if target was not found
        if (res[0] > res[1]) {
            res[0] = -1;
            res[1] = -1;
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // Test cases
        int[][] testNums = {
            {5, 7, 7, 8, 8, 10},
            {5, 7, 7, 8, 8, 10},
            {},
            {1}
        };
        int[] testTargets = {8, 6, 0, 1};
        int[][] expectedOutputs = {
            {3, 4},
            {-1, -1},
            {-1, -1},
            {0, 0}
        };

        for (int i = 0; i < testNums.length; i++) {
            int[] result = s.searchRange(testNums[i], testTargets[i]);
            if (Arrays.equals(result, expectedOutputs[i])) {
                System.out.println("Test case " + i + " succeeded");
            } else {
                System.out.println("Test case " + i + " failed: expected " + Arrays.toString(expectedOutputs[i]) + ", got " + Arrays.toString(result));
            }
        }
    }
}
