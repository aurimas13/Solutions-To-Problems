class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        // Initialize the matrix with -1
        int[][] matrix = new int[m][n];
        for (int[] row : matrix) {
            Arrays.fill(row, -1);
        }
        
        int top = 0, bottom = m - 1, left = 0, right = n - 1;
        ListNode current = head;
        
        while (current != null && top <= bottom && left <= right) {
            // Traverse top row
            for (int col = left; col <= right; col++) {
                if (current != null) {
                    matrix[top][col] = current.val;
                    current = current.next;
                } else {
                    return matrix;
                }
            }
            top++;
            
            // Traverse right column
            for (int row = top; row <= bottom; row++) {
                if (current != null) {
                    matrix[row][right] = current.val;
                    current = current.next;
                } else {
                    return matrix;
                }
            }
            right--;
            
            if (top <= bottom) {
                // Traverse bottom row
                for (int col = right; col >= left; col--) {
                    if (current != null) {
                        matrix[bottom][col] = current.val;
                        current = current.next;
                    } else {
                        return matrix;
                    }
                }
                bottom--;
            }
            
            if (left <= right) {
                // Traverse left column
                for (int row = bottom; row >= top; row--) {
                    if (current != null) {
                        matrix[row][left] = current.val;
                        current = current.next;
                    } else {
                        return matrix;
                    }
                }
                left++;
            }
        }
        
        return matrix;
    }
}