import java.util.*;

class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> rows = new ArrayList<>();
        Map<Integer, Integer> freq = new HashMap<>();
        
        // Count the frequency of each number
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        // Sort the numbers based on their frequency
        Integer[] sortedNums = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(sortedNums, (a, b) -> freq.get(b) - freq.get(a));
        
        for (int num : sortedNums) {
            // Check if the number can be placed in any existing row
            boolean placed = false;
            for (List<Integer> row : rows) {
                if (!row.contains(num)) {
                    row.add(num);
                    placed = true;
                    break;
                }
            }
            
            // If the number wasn't placed, create a new row for it
            if (!placed) {
                List<Integer> newRow = new ArrayList<>();
                newRow.add(num);
                rows.add(newRow);
            }
        }

        return rows;
    }
}
