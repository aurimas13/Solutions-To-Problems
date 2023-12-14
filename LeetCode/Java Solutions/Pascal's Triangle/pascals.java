import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();

        for (int row_num = 0; row_num < numRows; row_num++) {
            List<Integer> row = new ArrayList<>();
            for (int i = 0; i < row_num + 1; i++) {
                row.add(null);
            }
            row.set(0, 1);
            row.set(row.size() - 1, 1);

            for (int j = 1; j < row.size() - 1; j++) {
                row.set(j, triangle.get(row_num - 1).get(j - 1) + triangle.get(row_num - 1).get(j));
                System.out.println(row);
            }
            triangle.add(row);
        }

        return triangle;
    }

    public static void main(String[] args) {
        Solution instance = new Solution();
        List<List<Integer>> result = instance.generate(5);  // 5 -> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        System.out.println(result);
    }
}
