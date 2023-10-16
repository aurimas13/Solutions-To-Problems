import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        // handling the first two special cases
        if (rowIndex == 0) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            return row;
        } else if (rowIndex == 1) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            row.add(1);
            return row;
        }

        // creating the Pascal's Triangle
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(new ArrayList<>());
        triangle.get(0).add(1); // First row is always [1]

        // building the triangle row by row
        for (int i = 1; i <= rowIndex; i++) {
            List<Integer> row = new ArrayList<>();
            row.add(1);  // starting element of each row is 1

            // each triangle element is the sum of the two directly above it
            for (int j = 1; j < i; j++) {
                row.add(triangle.get(i - 1).get(j - 1) + triangle.get(i - 1).get(j));
            }

            row.add(1);  // ending element of each row is 1
            triangle.add(row);
        }

        // the question asks for the rowIndex-th row (0-indexed)
        return triangle.get(rowIndex);
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        List<Integer> row = obj.getRow(3); // Example usage
        System.out.println(row); // Should print [1, 3, 3, 1]
    }
}
