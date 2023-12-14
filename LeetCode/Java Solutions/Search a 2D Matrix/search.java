class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int[] row : matrix) {
            // If target is within the first and last element of the row, perform binary search.
            if (target >= row[0] && target <= row[row.length - 1]) {
                if (binarySearch(row, target)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean binarySearch(int[] row, int target) {
        // Perform binary search for the target within a row.
        int left = 0, right = row.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (row[mid] == target) {
                return true;
            } else if (row[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
