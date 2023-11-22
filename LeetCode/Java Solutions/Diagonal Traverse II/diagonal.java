import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        Map<Integer, List<Integer>> diagonalMap = new TreeMap<>();

        int totalCount = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.get(i).size(); j++) {
                diagonalMap.computeIfAbsent(i + j, k -> new ArrayList<>()).add(nums.get(i).get(j));
                totalCount++;
            }
        }

        int[] result = new int[totalCount];
        int index = 0;
        for (List<Integer> diagonal : diagonalMap.values()) {
            for (int i = diagonal.size() - 1; i >= 0; i--) {
                result[index++] = diagonal.get(i);
            }
        }

        return result;
    }
}

