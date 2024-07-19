import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        Set<Integer> minRow = new HashSet<>();
        Set<Integer> maxCol = new HashSet<>();
        
        // Find the minimum in each row
        for (int i = 0; i < m; i++) {
            int min = matrix[i][0];
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] < min) {
                    min = matrix[i][j];
                }
            }
            minRow.add(min);
        }
        
        // Find the maximum in each column
        for (int j = 0; j < n; j++) {
            int max = matrix[0][j];
            for (int i = 1; i < m; i++) {
                if (matrix[i][j] > max) {
                    max = matrix[i][j];
                }
            }
            maxCol.add(max);
        }
        
        // Find the intersection of minRow and maxCol
        List<Integer> result = new ArrayList<>();
        for (int num : minRow) {
            if (maxCol.contains(num)) {
                result.add(num);
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] matrix1 = {{3,7,8},{9,11,13},{15,16,17}};
        int[][] matrix2 = {{1,10,4,2},{9,3,8,7},{15,16,17,12}};
        int[][] matrix3 = {{7,8},{1,2}};
        
        System.out.println(sol.luckyNumbers(matrix1));  // Output: [15]
        System.out.println(sol.luckyNumbers(matrix2));  // Output: [12]
        System.out.println(sol.luckyNumbers(matrix3));  // Output: [7]
    }
}
