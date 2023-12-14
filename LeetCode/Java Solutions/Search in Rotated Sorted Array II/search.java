class Solution {
    public int search(int[] nums, int target) {
        // Initialize left and right pointers for binary search.
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // If the target is found, return its index.
            if (nums[mid] == target) {
                return mid;
            }

            // If the left half of the array is sorted.
            if (nums[left] <= nums[mid]) {
                // If target is in the sorted left half, search there.
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // Else, the right half of the array is sorted.
            else {
                // If target is in the sorted right half, search there.
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        // If target is not found, return -1.
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // Test cases
        int[][] testCasesNums = {
            {4, 5, 6, 7, 0, 1, 2},
            {4, 5, 6, 7, 0, 1, 2},
            {1},
            {1}
        };
        int[] testCasesTarget = {0, 3, 0, 1};
        int[] expectedOutput = {4, -1, -1, 0};

        for (int i = 0; i < testCasesNums.length; i++) {
            int result = s.search(testCasesNums[i], testCasesTarget[i]);
            assert result == expectedOutput[i] : "Test case " + i + " failed: expected " + expectedOutput[i] + ", got " + result;
            System.out.println("Test case " + i + " succeeded");
        }
    }
}


