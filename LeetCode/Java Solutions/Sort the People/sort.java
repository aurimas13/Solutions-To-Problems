import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        // Create an array of indices from 0 to names.length - 1
        Integer[] indices = new Integer[names.length];
        for (int i = 0; i < names.length; i++) {
            indices[i] = i;
        }
        
        // Sort indices based on heights in descending order
        Arrays.sort(indices, (a, b) -> heights[b] - heights[a]);
        
        // Create a result array and fill it with names based on the sorted indices
        String[] result = new String[names.length];
        for (int i = 0; i < names.length; i++) {
            result[i] = names[indices[i]];
        }
        
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.sortPeople(new String[]{"Mary", "John", "Emma"}, new int[]{180, 165, 170})));  // Output: ["Mary", "Emma", "John"]
        System.out.println(Arrays.toString(sol.sortPeople(new String[]{"Alice", "Bob", "Bob"}, new int[]{155, 185, 150})));   // Output: ["Bob", "Alice", "Bob"]
    }
}
